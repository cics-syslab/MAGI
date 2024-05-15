from magi.common.addon import hookimpl
from .config import Config
from magi.managers.info_manager import Directories
import shutil
import os

class ImageProcessing:

    @hookimpl
    def before_generating(self):
        # into_src, into_submission, test_list, package.json need to go into WORK_DIR
        shutil.copytree(Directories.MODULES_DIR / "ImageProcessing" / "into_src", Directories.WORK_DIR / "into_src")
        # os.system(f"cp -r {Directories.MODULES_DIR}/ImageProcessing/into_work_dir/* {Directories.WORK_DIR}")
        os.system(f"ln -s {Directories.MODULES_DIR}/ImageProcessing/into_work_dir/* {Directories.WORK_DIR}")
        # symlink node_modules into work_dir
        # os.symlink(Directories.MODULES_DIR / "ImageProcessing" / "node_modules", Directories.WORK_DIR / "node_modules", True)


