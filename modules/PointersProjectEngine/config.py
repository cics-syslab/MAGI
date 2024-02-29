from dataclasses import dataclass

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    # Source code default fields, these are changed depending on user's choice
    container_name: str = "container"  # The container name you are storing your items in
    container_type: str = "Container"  # The struct type your container is named
    item_name: str = "item"  # The name of the item you are working with (i.e. file, animal, etc)
    item_type: str = "Item"  # The struct type your item is named
    node_type: str = "Node"  # node to store your items, each being a "node"
    # For the main.c templates, these are the default values:
    descriptor_1: str = "Descriptor1"  # First choice of an adjective describing a given item
    descriptor_2: str = "Descriptor2"  # Second choice of an adjective describing a given item
    item_1: str = "item1"  # The name of your first item
    item_2: str = "item2"  # The name of your second item
    item_3: str = "item3"  # The name of your third item
    cluster_name: str = "ClusterName"
