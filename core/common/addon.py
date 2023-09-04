import importlib
from importlib import reload
import logging
import os.path as op
import yaml

from core.info.directories import Directories


class Addon:
    def __init__(self, name: str, category: str, root_dir: str):
        # This name is the name of the directory where the addon is located
        self.name: str = name

        # These fields will be loaded from info.yaml
        self.display_name: str = ""
        self.documentation: str = ""
        self.dependencies = None
        self.version: str = ""
        self.description: str = ""
        self.author: str = ""
        self.author_email: str = ""

        if category not in ["modules", "plugins"]:
            raise ValueError(f"Invalid category {category}")
        self.category = category
        self.root_dir = root_dir
        self.loaded = False
        self.module = None
        self.errored = False
        self.load_information()
        self.load_documentation()

    def load_information(self) -> bool:
        if not op.isfile(op.join(self.root_dir, "info.yaml")):
            return False
        logging.info(f"{self.name} has info.yaml with path {op.join(self.root_dir, 'info.yaml')}"
                     f"Loading from {op.join(self.root_dir, 'info.yaml')}")
        try:
            with open(op.join(self.root_dir, "info.yaml"), "r", encoding="utf-8") as f:
                info = yaml.safe_load(f)
                self.author = info.get("author", "")
                self.author_email = info.get("author_email", "")
                self.description = info.get("description", "")
                self.version = info.get("version", "")
                self.dependencies = info.get("dependencies", [])
                self.documentation = info.get("documentation", "")
                self.display_name = info.get("display_name", "")

        except Exception as e:
            logging.error(f"Error loading info.yaml for {self.name}: {e}")
            self.errored = True
            return False
        return True

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
            assert (self.module is not None)
        except Exception as e:
            logging.error(f"Error importing {self.name}: {e}")
            self.loaded = False
            self.errored = True
            return False
        logging.debug(f"Loaded addon {self.name} from {self.root_dir}")
        return self.loaded

    def load_documentation(self):
        if self.documentation == "" or self.documentation is None:
            return
        if not op.isfile(op.join(self.root_dir, self.documentation)):
            return
        logging.info(f"{self.name} has documentation with path {self.documentation}"
                     f"Loading from {op.join(self.root_dir, self.documentation)}")
        try:
            with open(op.join(self.root_dir, self.documentation), "r", encoding="utf-8") as f:
                self.documentation = f.read()
        except Exception as e:
            logging.error(f"Error loading documentation for {self.name}: {e}")
            self.documentation = ""
