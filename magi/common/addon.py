from __future__ import annotations

import importlib
import logging
import os.path as op
from dataclasses import dataclass

import dacite
import pluggy
import yaml

hookspec = pluggy.HookspecMarker("magi")
hookimpl = pluggy.HookimplMarker("magi")


class AddonSpec:
    def __init__(self):
        self.config = None

    @hookspec
    def before_generate(self):
        pass


    @hookspec
    def generate(self):
        """Hook for generating functionality."""

    @hookspec
    def after_generate(self):
        """Hook for actions after generating."""

    @hookspec
    def before_grading(self):
        """Hook for actions before grading."""

    @hookspec
    def grade(self):
        """Hook for grading functionality."""

    @hookspec
    def after_grading(self):
        """Hook for actions after grading."""

    @hookspec
    def generate_documentation(self):
        """Hook for generating documentation."""


@dataclass
class AddonInfo:
    name: str = ""
    documentation: str = ""
    # TODO: Implement dependencies
    # dependencies: list = field(default_factory=list)
    version: str = ""
    description: str = ""
    author: str = ""
    author_email: str = ""


class Addon:
    category = ""

    def __init__(self, name: str, root_dir: str):
        # This name is the name of the directory where the addon is located
        self.name: str = name

        self.info = AddonInfo()
        self.root_dir: str = root_dir
        self.loaded: bool = False
        self.imported_object: AddonSpec | None = None
        self.errored: bool = False
        self.load_information()
        # self.load_documentation()

    def load_information(self) -> bool:
        if not op.isfile(op.join(self.root_dir, "info.yaml")):
            return False
        logging.info(f"{self.name} has info.yaml with path {op.join(self.root_dir, 'info.yaml')}"
                     f"Loading from {op.join(self.root_dir, 'info.yaml')}")
        try:
            self.info = dacite.from_dict(AddonInfo, yaml.safe_load(
                open(op.join(self.root_dir, "info.yaml"), "r", encoding="utf-8")),
                                         config=dacite.Config(check_types=False))

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
            imported_module = importlib.import_module(f"{self.category}.{self.name}")
            if not hasattr(imported_module, self.name):
                logging.error(f"Module {self.name} does not have class {self.name}")
                return False

            self.imported_object = getattr(imported_module, self.name)()
            self.loaded = True
            assert (self.imported_object is not None)
        except Exception as e:
            logging.error(f"Error importing {self.name}: {e}", exc_info=True)
            self.loaded = False
            self.errored = True
            return False
        logging.debug(f"Loaded addon {self.name} from {self.root_dir}")
        return self.loaded

    def unload(self):
        if not self.loaded:
            return
        logging.debug(f"Unloading addon {self.name} from {self.root_dir}")

        self.imported_object = None
        self.loaded = False
        logging.debug(f"Unloaded addon {self.name} from {self.root_dir}")
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


class Module(Addon):
    category = "modules"


class Plugin(Addon):
    category = "plugins"
