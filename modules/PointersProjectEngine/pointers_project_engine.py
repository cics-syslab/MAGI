import os

from magi.common.addon import hookimpl
from .config import Config


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

    @hookimpl
    def generate(self):
        from magi.managers.info_manager import Directories
        from magi.utils.render import render_template
        render_template(
            os.path.join(Directories.SRC_PATH, "modules", "PointersProjectEngine", "templates", "test_list.yml.jinja"),
            Config.__dict__,
            os.path.join(Directories.WORK_DIR, "test_list.yml")
        )
        (Directories.OUTPUT_DIR / "solution" / ".keep").touch()
