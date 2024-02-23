from .config import Config
from magi.common.addon import hookimpl
import os


class PointersProjectEngine:
    def __init__(self):
        pass

    @hookimpl
    def before_generating(self):
        from magi.managers.info_manager import Directories
        from magi.utils.render import render_templates
        render_templates(
            os.path.join(Directories.SRC_PATH, "modules", "PointersProjectEngine", "templates"),
            Config.__dict__,
            os.path.join(Directories.WORK_DIR)
        )
