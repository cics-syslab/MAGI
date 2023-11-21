import datetime
import logging
import os
import os.path as op
import shutil

from core.info import Directories
from core.managers import SettingManager

logging = logging.getLogger("Generator")


def create_output_dir(output_parent_dir: str) -> str:
    """
    Create the output directory for the project files, and return the path to it. 
    To avoid overwriting the existing output directory when the directory existed, the output directory will be named with the current date and time.
    
    : param output_parent_dir: The parent directory to create the output directory in.
    : return: The path to the output directory.
    """
    if not output_parent_dir:
        raise Exception("No output directory provided")

    output_dir = op.join(output_parent_dir, SettingManager.BaseSettings.project_name)
    if os.path.isdir(output_dir):
        logging.warning(f'Output directory {output_dir} already exists, will be renamed with current date and time.')
        output_dir = output_dir + "-" + datetime.datetime.now().strftime('%Y%m%d-%H-%M-%S')

    logging.critical(f'Files will be produced to: {output_dir}')

    return output_dir


def pack_autograder(autograder_dir: str) -> None:
    """
    Pack the autograder directory into a zip file for uploading to Gradescope.

    : param autograder_dir: The directory to the autograder directory.
    : return: None
    """
    if not autograder_dir:
        raise Exception("No directory provided to make zip file")
    if not op.isdir(autograder_dir):
        raise NotADirectoryError()
    shutil.make_archive(op.join(autograder_dir, "..", "autograder"), 'zip', autograder_dir)

    logging.debug(f'Autograder packed to {op.join(autograder_dir, "..", "autograder.zip")}')


def generate_autograder(output_dir: str) -> None:
    """
    Generate the autograder files for the project under the given output directory.

    : param output_dir: The output directory to generate the autograder files under.
    : return: None
    """
    # Since the autograder depends on the framework, copy the framework core, enabled module, and enabled plugins to it.
    shutil.copytree(Directories.TEMPLATE_DIR, output_dir)
    output_source_dir = op.join(output_dir, "source")
    shutil.copytree(Directories.CORE_DIR, op.join(output_source_dir, "core"))
    shutil.copytree(Directories.LOGS_DIR, op.join(output_source_dir, "logs"))
    shutil.copy(op.join(Directories.SRC_PATH, "main.py"), output_source_dir)
    shutil.copytree(Directories.SETTINGS_DIR, op.join(output_source_dir, "settings"))
    if SettingManager.BaseSettings.enabled_module:
        enabled_module = SettingManager.BaseSettings.enabled_module
        os.mkdir(op.join(output_source_dir, "modules"))
        shutil.copytree(op.join(Directories.SRC_PATH, "modules", enabled_module),
                        op.join(output_source_dir, "modules", enabled_module))
    os.makedirs(op.join(output_source_dir, "plugins"), exist_ok=True)
    if len(SettingManager.BaseSettings.enabled_plugins) > 0:
        os.mkdir(op.join(output_source_dir, "plugins"))
        for enabled_plugin in SettingManager.BaseSettings.enabled_plugins:
            shutil.copytree(op.join(Directories.SRC_PATH, "plugins", enabled_plugin),
                            op.join(output_source_dir, "plugins", enabled_plugin))
    pack_autograder(output_source_dir)
    logging.info(f'Autograder successfully generated to {output_dir}')


def generate_output(output_parent_dir: str = None) -> None:
    """
    Generate the all project files under the given output directory. 

    : param output_parent_dir: The parent directory to create the output directory in.
    : return: None
    """
    if output_parent_dir is None:
        output_parent_dir = SettingManager.BaseSettings.output_dir

    # Save the settings before generating the output, useful for GUI
    SettingManager.save_settings()

    output_dir = create_output_dir(output_parent_dir)

    generate_autograder(output_dir)

    from .doc_generator import generate_documentation
    generate_documentation(op.join(output_dir, "documentation.md"))

    # Open the output directory if on Windows
    try:
        os.startfile(output_dir)
    except AttributeError:
        pass
    # TODO: add support for other OS
    # TODO: add option to skip opening the output directory
