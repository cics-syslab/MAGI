from dataclasses import dataclass, field
from typing import List


@dataclass
class BaseSettings:
    project_name: str = ""
    project_description: str = field(default_factory=str, metadata={"text_area": True})
    submission_files: List[str] = field(default_factory=list)
    output_dir: str = field(default_factory=lambda: "output", metadata={"excluded_from_ui": True})
    enabled_module: str = field(default_factory=str, metadata={"excluded_from_ui": True})
    enabled_plugins: List[str] = field(default_factory=list, metadata={"excluded_from_ui": True})
