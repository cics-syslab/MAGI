import importlib
import importlib.util
import logging as lg
logging = lg.getLogger('AddonManager')
import os
import os.path as op
import sys

from .setting_manager import SettingManager
from ..info.directories import Directories

def list_available(sub_dir: str) -> dict:
    # List all available modules/plugins 
    searching_dir = op.join(Directories.src_path, sub_dir)
    dirs = os.listdir(searching_dir)
    available = {}
    if sub_dir not in sys.path:
        sys.path.append(sub_dir)

    for _dir in dirs:
        logging.debug(f"Loading from {_dir}")
        if not op.exists(op.join(searching_dir, _dir, "__init__.py")):
            logging.warning(f"Module {_dir} does not have __init__.py")
            continue
        try:
            imported = importlib.import_module(_dir, sub_dir)
            logging.info(f"Imported {getattr(imported, 'name', 'None')} from {_dir}")
            available[_dir] = imported
        except Exception as e:
            logging.error(f"Error importing {_dir}: {e}")

    return available


class AddonManager:
    _dir_to_modules = {}
    _dir_to_plugins = {}
    _name_to_modules = {}
    _name_to_plugins = {}

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

    @property
    def enabled_module(self)->object:
        enabled_module_name = SettingManager.BaseSettings.enabled_module
        if not enabled_module_name:
            logging.debug("No enabled module")
            return None
        if enabled_module_name not in self.available_modules.keys():
            logging.error(f"Module {enabled_module_name} not found")
            return None
        return self._name_to_modules[enabled_module_name]

    @property
    def enabled_plugins(self)->list:
        enabled_plugins_names = SettingManager.BaseSettings.enabled_plugins
        if not enabled_plugins_names:
            logging.debug("No enabled plugins")
            return []
        enabled_plugins = []
        for plugin_name in enabled_plugins_names:
            if plugin_name not in self.available_plugins.keys():
                logging.error(f"Plugin {plugin_name} not found")
                continue
            enabled_plugins.append(self._name_to_plugins[plugin_name])
        return enabled_plugins
    
    def run_attr_for_all(self, attr):
        all_addon = [self.enabled_module] + self.enabled_plugins
        rtn = []
        for addon in all_addon:
            if not addon:
                continue
            func = getattr(addon, attr, None)
            if func:
                logging.info(f"Running {attr} for {addon.name}")
                rtn.append(func())
            else:
                logging.debug(f"Addon {addon.name} does not have {attr},skipped")
        return rtn
    
    def setup(self):
        pass

    def generate(self):
        self.run_attr_for_all("generating")

    def grade(self):
        self.run_attr_for_all("before_grading")
        self.run_attr_for_all("grade")
        self.run_attr_for_all("after_grading")

    def generate_documentation(self):
        return self.run_attr_for_all("generate_documentation")