from dataclasses import dataclass, field
from core.managers import SettingManager
# from .decorators import register_settings

@SettingManager.register
@dataclass
class Config:
    # Source code default fields
    # project_name: str = "My Project"
    CONTAINER: str = "Container"
    CONTAINER_TYPE: str = "Container Type"
    ITEM_TYPE: str = "Item Type"
    ITEM: str = "Item"
    LINKED_LIST: str = "Linked List"
    # For the main.c template, these are the default values:
    DESCRIPTOR1: str = "Descriptor1"
    DESCRIPTOR2: str = "Descriptor2"
    ITEM1: str = "Item1"
    ITEM2: str = "Item2"
    ITEM3: str = "Item3"