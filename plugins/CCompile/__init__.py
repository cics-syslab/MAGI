#from CCompile import before_grading, Config
from .CCompile import Config
name = "CCompile"
from core.managers.setting_manager import SettingManager
config = SettingManager.register(Config)