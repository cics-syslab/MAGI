import importlib
import logging
import os.path as op
from dataclasses import dataclass
import yaml


@dataclass
class AddonInfo:
    name: str = ""
    documentation: str = ""
    # TODO: Implement dependencies
    #dependencies: list = field(default_factory=list)
    version: str|float|int = ""
    description: str = ""
    author: str = ""
    author_email: str = ""


class Addon:
    def __init__(self, name: str, category: str, root_dir: str):
        # This name is the name of the directory where the addon is located
        self.name: str = name

        self.info = AddonInfo()
        if category not in ["modules", "plugins"]:
            raise ValueError(f"Invalid category {category}")
        self.category = category
        self.root_dir = root_dir
        self.loaded = False
        self.module = None
        self.errored = False
        self.load_information()
        # self.load_documentation()

    # TODO: load with some library instead, dataconf has too many issues
    def load_information(self) -> bool:
        if not op.isfile(op.join(self.root_dir, "info.yaml")):
            return False
        logging.info(f"{self.name} has info.yaml with path {op.join(self.root_dir, 'info.yaml')}"
                     f"Loading from {op.join(self.root_dir, 'info.yaml')}")
        try:
            self.info = AddonInfo(**yaml.load(open(op.join(self.root_dir, "info.yaml"), "r", encoding="utf-8"), Loader=yaml.FullLoader))

        except Exception as e:
            logging.error(f"Error loading info.yaml for {self.name}: {e}")
            self.errored = True

    def load(self) -> bool:
        if self.errored:
            return False
        if self.loaded:
            return True
        logging.debug(f"Loading addon {self.name} from {self.root_dir}")

        if not op.isfile(op.join(self.root_dir, "__init__.py")):
            logging.warning(f"Module {self.name} does not have __init__.py")

        try:
            logging.debug(f"Importing {self.name} from {self.category}")

            self.module = importlib.import_module(f"{self.category}.{self.name}")
            self.loaded = True
            from magi.managers import AddonManager
            AddonManager.plugin_manager.register(self.module)
            assert (self.module is not None)
        except Exception as e:
            logging.error(f"Error importing {self.name}: {e}", exc_info=True)
            self.loaded = False
            self.errored = True
            return None
        logging.debug(f"Loaded addon {self.name} from {self.root_dir}")
        return self.loaded

    # Do not load documentation content for now 
    # def load_documentation(self):
    #     if self.documentation == "" or self.documentation is None:
    #         return
    #     if not op.isfile(op.join(self.root_dir, self.documentation)):
    #         return
    #     logging.info(f"{self.name} has documentation with path {self.documentation}"
    #                  f"Loading from {op.join(self.root_dir, self.documentation)}")
    #     try:
    #         with open(op.join(self.root_dir, self.documentation), "r", encoding="utf-8") as f:
    #             self.documentation = f.read()
    #     except Exception as e:
    #         logging.error(f"Error loading documentation for {self.name}: {e}")
    #         self.documentation = ""
