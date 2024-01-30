from .config import Config
from .gen_doc import generate_documentation
from core.common.addon import hookimpl
from .grader import grade


class NetworkProjectEngine:
    def __init__(self):
        self.config = Config

    @hookimpl
    def generate_documentation(self):
        generate_documentation()

    @hookimpl
    def grade(self):
        grade()
