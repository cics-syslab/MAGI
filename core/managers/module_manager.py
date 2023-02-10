import importlib
import importlib.util
import logging
import os
import os.path as op
import sys

from .setting_manager import SettingManager


def list_available(sub_dir: str) -> dict:
    # List all available modules/plugins 
    searching_dir = op.join(SettingManager.Directories.src_path, sub_dir)
    dirs = os.listdir(searching_dir)
    available = {}
    if sub_dir not in sys.path:
        sys.path.append(sub_dir)

    for _dir in dirs:
        logging.info(f"Loading from {_dir}")
        if not op.exists(op.join(searching_dir, _dir, "__init__.py")):
            logging.debug(f"Module {_dir} does not have __init__.py")
            continue

        imported = importlib.import_module(_dir, sub_dir)
        logging.debug(f"Imported {getattr(imported, 'name', 'None')} from {_dir}")
        available[_dir] = imported
    return available


class ModuleManager:
    _dir_to_modules = {}
    _dir_to_plugins = {}
    _name_to_modules = {}
    _name_to_plugins = {}

    enabled_module = None
    enabled_plugins = []

    @property
    def available_modules(self):
        if self._name_to_modules == {}:
            self._dir_to_modules = list_available("modules")
            self._name_to_modules = {module.name: module for module in self._dir_to_modules.values()}
        return self._name_to_modules

    @property
    def available_plugins(self):
        if self._name_to_plugins == {}:
            self._dir_to_plugins = list_available("plugins")
            self._name_to_plugins = {plugin.name: plugin for plugin in self._dir_to_plugins.values()}
        return self._name_to_plugins

    def init_run(self):
        enabled_module = SettingManager.BaseSettings.enabled_module
        if enabled_module not in self.available_modules.keys():
            # logging.fatal
            pass
        self.enabled_module = self._name_to_modules[enabled_module]
        for enabled_plugin in SettingManager.BaseSettings.enabled_plugins:
            if enabled_plugin not in self.available_plugins_name:
                # logging.fatal
                pass

            self.enabled_module[enabled_plugin] = self._name_to_plugins[enabled_plugin]

    def run_attr_for_all(self, attr):
        for module in self.enabled_module:
            func = getattr(module, attr)
            if func:
                func()
        for plugin in self.enabled_plugins:
            func = getattr(plugin, attr)
            if func:
                func()

    def setup(self):
        pass

    def generate(self):
        self.run_attr_for_all("generating")

    def grade(self):
        self.run_attr_for_all("before_grading")
        self.run_attr_for_all("grading")
        self.run_attr_for_all("after_grading")
