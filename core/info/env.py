from dataclasses import dataclass


@dataclass
class Env:
    in_gradescope: bool = False
    in_docker: bool = False


_instance = Env()
