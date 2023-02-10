from dataclasses import dataclass, field


# @SettingManager.register
@dataclass
class Config:
    question_format: str = ""
    qa: str = field(default_factory=str,
                    metadata={"excluded_from_ui": True, "file_editor": "modules/NetworkProjectEngine/QA.py"})
