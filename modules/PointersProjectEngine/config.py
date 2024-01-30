from dataclasses import dataclass, field
from core.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    # Source code default fields, these are changed depending on user's choice
    container_name: str = "Container"  # The container name you are storing your items in
    container_type: str = "Container Type"  # The struct type your container is named
    item_name: str = "Item"  # The name of the item you are working with (i.e. file, animal, etc)
    item_type: str = "Item Type"  # The struct type your item is named
    linked_list_name: str = "Linked List"  # Linked list to store your items, each being a "node"
    # For the main.c templates, these are the default values:
    descriptor_1: str = "Descriptor1"  # First choice of an adjective describing a given item
    descriptor_2: str = "Descriptor2"  # Second choice of an adjective describing a given item
    item_1: str = "Item1"  # The name of your first item
    item_2: str = "Item2"  # The name of your second item
    item_3: str = "Item3"  # The name of your third item
    project_name: str = "Project Name"
