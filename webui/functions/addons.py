import os
from time import sleep

from jinja2 import Environment, PackageLoader, select_autoescape

from streamlit import session_state


env = Environment(
    loader=PackageLoader("webui"),
    autoescape=select_autoescape()
)
template = env.get_template("addon.jinja2")


def render_addon_page(addon):
    if addon is None:
        return
    content = template.render(addon=addon)
    filepath = get_addon_page_path(addon)
    if not os.path.isfile(filepath):
        with open(filepath, "w+") as f:
            f.write(content)
    else:
        with open(filepath, "r") as f:
            old_content = f.read()
        if old_content != content:
            with open(filepath, "w") as f:
                f.write(content)


def get_addon_page_path(addon):
    prefix = "1_" if addon.category == "modules" else "2_"
    filename = f"{prefix}{addon.name}.py"
    filepath = os.path.join("webui", "pages", filename)
    return filepath


def update_pages():
    update_addon_lock = session_state.update_addon_lock
    SettingManager = session_state.SettingManager
    AddonManager = session_state.AddonManager
    InfoManager = session_state.InfoManager
    with update_addon_lock:
        print("Updating pages")
        
        files = os.listdir(InfoManager.Directories.SRC_PATH / "webui" / "pages")
        # print("enabled module", AddonManager.enabled_module.name)
        # print("enabled plugins", AddonManager.enabled_plugins)
        # print("files", files)

        for file in files:
            if file.startswith("1_"):
                addon_name = file.split(".")[0][2:]
                if addon_name != SettingManager.BaseSettings.enabled_module:
                    os.remove(os.path.join("webui", "pages", file))
            elif file.startswith("2_"):
                addon_name = file.split(".")[0][2:]
                if addon_name not in SettingManager.BaseSettings.enabled_plugins:
                    os.remove(os.path.join("webui", "pages", file))
        # otherwise, the pages will be updated too quickly and streamlit will not be able to keep up
        # sleep(0.1)
        for addon in [AddonManager.enabled_module] + AddonManager.enabled_plugins:
            print("Rendering addon page", addon)
            render_addon_page(addon)
        
        
        print("Pages updated")
