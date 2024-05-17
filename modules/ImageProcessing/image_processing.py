from magi.common.addon import hookimpl
from .config import Config
from magi.managers.info_manager import Directories
import shutil
import os

class ImageProcessing:

    @hookimpl
    def before_generating(self):
        # into_src needs to go into src, into_work_dir needs to go into work dir
        shutil.copytree(Directories.MODULES_DIR / "ImageProcessing" / "into_src", Directories.WORK_DIR / "into_src")
        os.system(f"cp -r {Directories.MODULES_DIR}/ImageProcessing/into_work_dir/* {Directories.WORK_DIR}")


