import logging
import os
import os.path as op
from typing import Any

from core._private.singleton import lazy_singleton
from core.common.addon import Addon
from core.info.directories import Directories

logging = logging.getLogger('AddonManager')


def list_available_addons(subdirectory: str) -> list:
    """
    List all available addons in the given subdirectory

    :param subdirectory: The subdirectory to search for addons, either "modules" or "plugins"
    :return: A list of Addon objects
    """
    searching_dir = op.join(Directories.SRC_PATH, subdirectory)
    dirs = os.listdir(searching_dir)
    available = []

    for sub_dir in dirs:
        if not op.exists(op.join(searching_dir, sub_dir, "info.yaml")):
            logging.warning(f"Skipping {sub_dir} because info.yaml does not exist")
            continue
        try:
            addon = Addon(sub_dir, subdirectory, op.join(searching_dir, sub_dir))
            available.append(addon)
            logging.info(f"Found addon {addon.name} in {addon.root_dir}")

        except Exception as e:
            # print original traceback
            logging.error(f"Error importing {sub_dir}: {e}", exc_info=True)

    return available


@lazy_singleton
class AddonManager:
    def __init__(self):
        self.available_modules = list_available_addons("modules")
        self.available_plugins = list_available_addons("plugins")
        self._name_to_modules = {addon.name: addon for addon in self.available_modules}
        self._name_to_plugins = {addon.name: addon for addon in self.available_plugins}

    @property
    def available_plugin_names(self):
        return list(plugin.name for plugin in self.available_plugins if not plugin.errored)

    @property
    def available_module_names(self):
        return list(module.name for module in self.available_modules if not module.errored)

    @property
    def enabled_module(self) -> Any | None:
        from core.managers import SettingManager
        enabled_module_name = SettingManager.BaseSettings.enabled_module
        if not enabled_module_name:
            logging.debug("No enabled module")
            return None
        if enabled_module_name not in self._name_to_modules.keys():
            logging.error(f"Module {SettingManager.BaseSettings.enabled_module} not found")
            return None
        if self._name_to_modules[SettingManager.BaseSettings.enabled_module].load():
            return self._name_to_modules[SettingManager.BaseSettings.enabled_module]

        logging.error(f"Error loading module {SettingManager.BaseSettings.enabled_module}")
        SettingManager.BaseSettings.enabled_module = "None"
        return None

    @property
    def enabled_plugins(self) -> list:
        from core.managers import SettingManager
        enabled_plugins_names = SettingManager.BaseSettings.enabled_plugins
        if not enabled_plugins_names:
            logging.debug("No enabled plugins")
            return []
        enabled_plugins = []
        for plugin_name in enabled_plugins_names:
            if plugin_name not in self._name_to_plugins.keys():
                logging.error(f"Plugin {plugin_name} not found")
                continue
            if self._name_to_plugins[plugin_name].load():
                enabled_plugins.append(self._name_to_plugins[plugin_name])
            else:
                logging.error(f"Error loading plugin {plugin_name}")
                SettingManager.BaseSettings.enabled_plugins.remove(plugin_name)
        return enabled_plugins

    def run_attr_for_all(self, attr):
        all_addon = [self.enabled_module] + self.enabled_plugins
        rtn = []
        for addon in all_addon:
            if addon is None:
                continue

            module = addon.module
            if not module:
                continue
            func = getattr(module, attr, None)
            if func:
                logging.info(f"Running {attr} for {addon.name}")
                try:
                    rtn.append(func())
                except Exception as e:
                    logging.error(f"Error running {attr} for {addon.name}: {e}", exc_info=True)

            else:
                logging.debug(f"Addon {addon.name} does not have {attr},skipped")
        return rtn

    # TODO: implement setup for each addon
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
