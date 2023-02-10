from dataclasses import dataclass


@dataclass
class Metadata:
    id: int = 0
    created_at: str = ""


instance = Metadata()
