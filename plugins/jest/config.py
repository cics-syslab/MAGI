from dataclasses import dataclass, field
from magi.managers import SettingManager
from magi.managers.info_manager import Directories

@SettingManager.register
@dataclass
class Config:
    assertion_exec: str = field(default=f"node ./node_modules/jest/bin/jest.js --testPathPattern=.field(default=)/src --json --outputFile out.json", metadata={"help": "heyo"})
    coverage_exec: str = field(default=f"node ./node_modules/jest/bin/jest.js --testPathPattern=.field(default=)/src --coverage", metadata={"help": "heyo"})
    linting_exec: str = field(default=f"node ./node_modules/eslint/bin/eslint.js --config .eslintrc --max-warnings 0 ./src", metadata={"help": "heyo"})
    linting: float = field(default=2.5, metadata={"help": "heyo"})
    assertions: float = field(default=85, metadata={"help": "heyo"})
    coverage: float = field(default=12.5, metadata={"help": "heyo"})
    branch_coverage: float = field(default=50, metadata={"help": "heyo"})
    function_coverage: float = field(default=100, metadata={"help": "heyo"})
    statement_coverage: float = field(default=80, metadata={"help": "heyo"})
    coverage_timeout: float = field(default=120, metadata={"help": "heyo"})
    assertion_timeout: float = field(default=120, metadata={"help": "heyo"})
    eslintrc: str = field(default="plugins/jest/.eslintrc",
                          metadata={"excluded_from_ui": True,
                                    "file_editor": "plugins/jest/.eslintrc"})

