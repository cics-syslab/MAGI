from dataclasses import dataclass

from core.managers import SettingManager


@dataclass
class _Settings:
    pass


Settings: _Settings = SettingManager.register(_Settings, "base.yaml")
