from __future__ import annotations

import logging
import os
import os.path as op
import shutil
from pathlib import Path

from magi.managers import SettingManager
from magi.managers.info_manager import Directories

logging = logging.getLogger("Generator")


# def create_output_dir(output_parent_dir: str) -> str:
#     """
#     Create the output directory for the project files, and return the path to it.
#     To avoid overwriting the existing output directory when the directory existed,
#     the output directory will be named with the current date and time.
#
#     : param output_parent_dir: The parent directory to create the output directory in.
#     : return: The path to the output directory.
#     """
#     if not output_parent_dir:
#         raise Exception("No output directory provided")
#
#     output_dir = op.join(output_parent_dir, SettingManager.BaseSettings.project_name)
#     if os.path.isdir(output_dir):
#         logging.warning(f'Output directory {output_dir} already exists, will be renamed with current date and time.')
#         output_dir = output_dir + "-" + datetime.datetime.now().strftime('%y%m%d%H%M%S')
#
#     logging.critical(f'Files will be produced to: {output_dir}')
#
#     return output_dir


def make_zip(target_dir: str | Path, zip_file_name: str) -> None:
    """
    Pack the directory into a zip file in its parent directory.

    : param target_dir: The directory to the autograder directory.
    : param zip_file_name: The name of the zip file to create.
    : return: None
    """
    if not target_dir:
        raise Exception("No directory provided to make zip file")
    if not op.isdir(target_dir):
        raise NotADirectoryError()
    if not isinstance(target_dir, Path):
        target_dir = Path(target_dir)
    shutil.make_archive(str(target_dir.parent / zip_file_name), 'zip', target_dir)

    logging.info(f'{target_dir} packed to {op.join(target_dir.parent, f"{zip_file_name}.zip")}')


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

    clone_dirs = ['magi', 'settings', 'workdir']
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
    make_zip(output_source_dir, "autograder")

    logging.info(f'Autograder successfully generated to {output_dir}')


def reset_dir(dir_path: Path) -> None:
    for file in dir_path.iterdir():
        if file.name == ".gitkeep":
            continue

        if file.is_file():
            file.unlink()
        else:
            shutil.rmtree(file)


def reset_output_dir() -> None:
    """
    Reset the output directory to its initial state.

    : return: None
    """
    from magi.managers import InfoManager
    output_dir = InfoManager.Directories.OUTPUT_DIR
    reset_dir(output_dir)
    logging.info(f'Output directory {output_dir} reset.')
    for subdir in ["source", "solution", "dist", "misc"]:
        os.makedirs(op.join(output_dir, subdir), exist_ok=True)


def reset_workdir() -> None:
    from magi.managers import InfoManager
    workdir = InfoManager.Directories.WORK_DIR
    reset_dir(workdir)


def generate_documentation(file_path: str | Path) -> None:
    """
    Generate the documentation for the project, and write it to the given file path.

    Iterates through all addons and calls their generate_documentation() method. If none of the addons have documentation, then no documentation is generated.

    : param file_path: The path to the file to write the documentation to.
    : return: None
    """
    from magi.managers import AddonManager
    from magi.managers import SettingManager
    docs = AddonManager.generate_documentation()

    if not docs:
        return

    doc_string = f"# {SettingManager.BaseSettings.project_name} \n \n {SettingManager.BaseSettings.project_description} \n \n"

    doc_string += "\n".join(docs)
    with open(file_path, "w+", encoding="utf-8") as f:
        f.write(doc_string)

    return


def generate_output(output_dir: str = None) -> None:
    """
    Generate the all project files under the given output directory.

    : param output_parent_dir: The parent directory to create the output directory in.
    : return: None
    """
    from magi.managers import AddonManager
    if output_dir is None:
        output_dir = SettingManager.BaseSettings.output_dir

    # Save the settings before generating the output, useful for GUI
    SettingManager.save_settings()

    reset_output_dir()
    reset_workdir()
    output_dir = Path(output_dir)
    AddonManager.before_generating()

    shutil.copytree(Directories.TEMPLATE_DIR / "source", output_dir / "source", dirs_exist_ok=True)
    generate_autograder(output_dir)
    AddonManager.generate()
    AddonManager.after_generating()

    if len(os.listdir(output_dir / "solution")) != 0:
        make_zip(output_dir / "solution", "solution")

    if len(os.listdir(output_dir / "misc")) != 0:
        make_zip(output_dir / "misc", "misc")

    if len(os.listdir(output_dir / "dist")) != 0:
        make_zip(output_dir / "dist", "dist")

    generate_documentation(output_dir / "documentation.md")

    logging.info(f'Files successfully generated to {output_dir}')
