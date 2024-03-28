import json
from dataclasses import asdict
from enum import Enum
from pathlib import Path

import dacite
from dacite import from_dict


def serialize(instance: object, filepath: str | Path):
    """
    Dump the dataclass instance to the file

    :param instance: The dataclass instance
    :param filepath: The path to the file
    :return: None
    """
    json.dump(asdict(instance), open(
        filepath, "w+", encoding="utf-8"), indent=4)


def deserialize(cls: type, filepath: str | Path):
    """
    Load the dataclass from the file

    :param cls:  The dataclass to load
    :param filepath:  The path to the file
    :return:  The loaded instance
    """
    return from_dict(cls, json.load(open(filepath, "r", encoding="utf-8")), config=dacite.Config(cast=[Enum]))
