from __future__ import annotations

import logging
import os
import os.path as op
from typing import List

import pluggy

from magi.common.addon import AddonSpec, Module, Plugin
from magi.managers.info_manager import Directories

logging = logging.getLogger('AddonManager')
pm = pluggy.PluginManager("magi")
pm.add_hookspecs(AddonSpec)


def list_available_addons(addon_category: str) -> List[Module | Plugin]:
    """
    List all available addons in the given subdirectory

    :param addon_category: The subdirectory to search for addons, either "modules" or "plugins"
    :return: A list of Addon objects
    """
    searching_dir = op.join(Directories.SRC_PATH, addon_category)
    dirs = os.listdir(searching_dir)
    available = []

    for sub_dir in dirs:
        if not op.exists(op.join(searching_dir, sub_dir, "info.yaml")):
            logging.warning(f"Skipping {sub_dir} because info.yaml does not exist")
            continue
        if addon_category == "modules":
            from magi.common.addon import Module as Addon
        elif addon_category == "plugins":
            from magi.common.addon import Plugin as Addon
        else:
            raise ValueError(f"Invalid addon category {addon_category}")

        try:
            addon = Addon(sub_dir, op.join(searching_dir, sub_dir))
            available.append(addon)
            logging.info(f"Found addon {addon.name} in {addon.root_dir}")

        except Exception as e:
            # print original traceback
            logging.error(f"Error importing {sub_dir}: {e}", exc_info=True)

    return available


available_modules = list_available_addons("modules")
available_plugins = list_available_addons("plugins")
_name_to_modules = {addon.name: addon for addon in available_modules}
_name_to_plugins = {addon.name: addon for addon in available_plugins}
enabled_module = None
enabled_plugins = []


def get_available_plugin_names():
    return list(plugin.name for plugin in available_plugins if not plugin.errored)


def get_available_module_names():
    return list(module.name for module in available_modules if not module.errored)


def unload_addon(addon):
    pm.unregister(addon.imported_object)
    addon.unload()
    from magi.managers import SettingManager
    SettingManager.save_settings_for(addon.name)


def update_enabled_module() -> Module | None:
    from magi.managers import SettingManager
    new_enabled_module_name = SettingManager.BaseSettings.enabled_module

    global enabled_module
    # If unchanged, return the current enabled module
    if enabled_module is not None and enabled_module.name == new_enabled_module_name:
        return enabled_module

    # unload the current enabled module
    if enabled_module:
        unload_addon(enabled_module)
    enabled_module = None

    if not new_enabled_module_name or new_enabled_module_name == "None":
        logging.debug("No enabled module")
        return None

    if new_enabled_module_name not in _name_to_modules.keys():
        logging.error(f"Module {SettingManager.BaseSettings.enabled_module} not found")
        return None

    if _name_to_modules[SettingManager.BaseSettings.enabled_module].load():
        enabled_module = _name_to_modules[SettingManager.BaseSettings.enabled_module]
        pm.register(enabled_module.imported_object)
        return enabled_module
    logging.error(f"Error loading module {SettingManager.BaseSettings.enabled_module}", exc_info=True)
    # raise ValueError(f"Error loading module {SettingManager.BaseSettings.enabled_module}")
    SettingManager.BaseSettings.enabled_module = "None"
    enabled_module = None

    return None


def update_enabled_plugins() -> List[Plugin]:
    from magi.managers import SettingManager
    new_enabled_plugin_names = SettingManager.BaseSettings.enabled_plugins

    global enabled_plugins
    # Convert enabled_plugins names to a set for easier comparison
    current_enabled_plugin_names = {plugin.name for plugin in enabled_plugins}

    # Find plugins to unload (those that are currently enabled but not in the new list)
    plugins_to_unload = current_enabled_plugin_names - set(new_enabled_plugin_names)
    for plugin_name in plugins_to_unload:
        plugin_to_unload = _name_to_plugins[plugin_name]
        if plugin_to_unload:
            unload_addon(plugin_to_unload)
            enabled_plugins.remove(plugin_to_unload)

    # Find and load new plugins (those that are in the new list but not currently enabled)
    for plugin_name in new_enabled_plugin_names:
        if plugin_name not in current_enabled_plugin_names:
            if plugin_name in _name_to_plugins and _name_to_plugins[plugin_name].load():
                pm.register(_name_to_plugins[plugin_name].imported_object)
                enabled_plugins.append(_name_to_plugins[plugin_name])
            else:
                logging.error(f"Error loading plugin {plugin_name}")
                SettingManager.BaseSettings.enabled_plugins.remove(plugin_name)

    return enabled_plugins


# def run_attr_for_all(attr):
#     all_addon = [get_enabled_module()] + get_enabled_plugins()
#     rtn = []
#     for addon in all_addon:
#         if addon is None:
#             continue
#
#         module = addon.imported_object
#         if not module:
#             continue
#         func = getattr(module, attr, None)
#         if func:
#             logging.info(f"Running {attr} for {addon.name}")
#             try:
#                 rtn.append(func())
#             except Exception as e:
#                 logging.error(f"Error running {attr} for {addon.name}: {e}", exc_info=True)
#
#         else:
#             logging.debug(f"Addon {addon.name} does not have {attr},skipped")
#     return rtn


def before_generating():
    pm.hook.before_generating()


def after_generating():
    pm.hook.after_generating()


def generate():
    return pm.hook.generate()


def grade():
    from . import TestManager
    grading_steps = [
        pm.hook.before_grading,
        pm.hook.grade,
        pm.hook.after_grading,
    ]
    for step in grading_steps:
        if TestManager.status.all_failed:
            logging.info("All failed, skipping grading")
            return
        step()


def generate_documentation():
    return pm.hook.generate_documentation()
