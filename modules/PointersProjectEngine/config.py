from dataclasses import dataclass, field

from magi.managers import SettingManager


@SettingManager.register
@dataclass
class Config:
    # Source code default fields, these are changed depending on user's choice
    container_name: str = field(default="container",
                                metadata={"help": "The container name you are storing your items in."})
    container_type: str = field(default="Container", metadata={"help": "The struct type your container is named."})
    item_name: str = field(default="item",
                           metadata={"help": "The name of the item you are working with (i.e. file, animal, etc)."})
    item_type: str = field(default="Item", metadata={"help": "The struct type your item is named."})
    node_type: str = field(default="Node", metadata={"help": "Node to store your items, each being a 'node'."})
    # For the main.c templates, these are the default values:
    container1: str = field(default="Container1",
                            metadata={"help": "First choice of an adjective describing a given item."})
    container2: str = field(default="Container2",
                            metadata={"help": "Second choice of an adjective describing a given item."})
    item1: str = field(default="item1", metadata={"help": "The name of your first item."})
    item2: str = field(default="item2", metadata={"help": "The name of your second item."})
    item3: str = field(default="item3", metadata={"help": "The name of your third item."})
    cluster_name: str = field(default="ClusterName", metadata={"help": "Name of the cluster."})
