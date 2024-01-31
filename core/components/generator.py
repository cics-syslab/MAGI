from __future__ import annotations

import datetime
import logging
import os
import os.path as op
import shutil
from pathlib import Path

from core.managers import SettingManager
from core.managers.info_manager import Directories

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
        output_dir = output_dir + "-" + datetime.datetime.now().strftime('%y%m%d%H%M%S')

    logging.critical(f'Files will be produced to: {output_dir}')

    return output_dir


def pack_autograder(autograder_dir: str | Path) -> None:
    """
    Pack the autograder directory into a zip file for uploading to Gradescope.

    : param autograder_dir: The directory to the autograder directory.
    : return: None
    """
    if not autograder_dir:
        raise Exception("No directory provided to make zip file")
    if not op.isdir(autograder_dir):
        raise NotADirectoryError()
    if not isinstance(autograder_dir, Path):
        autograder_dir = Path(autograder_dir)
    zip_name = "autograder"
    shutil.make_archive(str(autograder_dir.parent / zip_name), 'zip', autograder_dir)

    logging.info(f'Autograder packed to {op.join(autograder_dir.parent, "autograder.zip")}')


def generate_autograder(output_dir: str | Path) -> None:
    """
    Generate the autograder files for the project under the given output directory.

    : param output_dir: The output directory to generate the autograder files under.
    : return: None
    """
    if output_dir is None:
        logging.error("No output directory provided")
        return

    if not isinstance(output_dir, Path):
        output_dir = Path(output_dir)

    # Since the autograder depends on the framework, copy the framework core, enabled module, and enabled plugins to it.
    # shutil.copytree(Directories.TEMPLATE_DIR, output_dir)
    output_source_dir = output_dir / "source"

    empty_dirs = ['logs', 'modules', 'plugins', ]
    for empty_dir in empty_dirs:
        os.makedirs(output_source_dir / empty_dir, exist_ok=True)
        Path.touch(output_source_dir / empty_dir / '.gitkeep', exist_ok=True)

    clone_dirs = ['core', 'settings', 'workdir']
    for clone_dir in clone_dirs:
        shutil.copytree(Directories.SRC_PATH / clone_dir, output_source_dir / clone_dir)

    clone_files = ['main.py']
    for clone_file in clone_files:
        shutil.copy(Directories.SRC_PATH / clone_file, output_source_dir)

    if SettingManager.BaseSettings.enabled_module and SettingManager.BaseSettings.enabled_module != "None":
        enabled_module = SettingManager.BaseSettings.enabled_module
        shutil.copytree(op.join(Directories.SRC_PATH, "modules", enabled_module),
                        op.join(output_source_dir, "modules", enabled_module))

    if len(SettingManager.BaseSettings.enabled_plugins) > 0:
        for enabled_plugin in SettingManager.BaseSettings.enabled_plugins:
            shutil.copytree(Directories.SRC_PATH / "plugins" / enabled_plugin,
                            output_source_dir / "plugins" / enabled_plugin)
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

    # output_dir = create_output_dir(output_parent_dir)
    output_dir = Path(output_parent_dir)

    shutil.rmtree(output_dir / "source", ignore_errors=True)
    shutil.copytree(Directories.TEMPLATE_DIR / "source", output_dir / "source")
    from core.managers import AddonManager
    AddonManager.generate()
    generate_autograder(output_dir)

    from .doc_generator import generate_documentation
    generate_documentation(op.join(output_dir, "documentation.md"))
