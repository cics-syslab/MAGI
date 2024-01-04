from dataclasses import dataclass

from magi._private.singleton import overwrite_singleton


@overwrite_singleton
@dataclass
class Env:
    in_gradescope: bool = False
    in_docker: bool = False


