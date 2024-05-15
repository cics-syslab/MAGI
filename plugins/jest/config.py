from dataclasses import dataclass, field
from magi.managers import SettingManager
from magi.managers.info_manager import Directories

@SettingManager.register
@dataclass
class Config:
    assertion_exec = f"node ./node_modules/jest/bin/jest.js --testPathPattern=./src --json --outputFile out.json"
    coverage_exec = f"node ./node_modules/jest/bin/jest.js --testPathPattern=./src --coverage"
    linting_exec = f"node ./node_modules/eslint/bin/eslint.js --config .eslintrc --max-warnings 0 ./src"
    linting = 2.5
    assertions = 85
    coverage = 12.5
    branch_coverage = 50
    function_coverage = 100
    statement_coverage = 80
    coverage_timeout = 120
    assertion_timeout = 120
    # test_list: str = field(default="plugins/jest/test_list.toml",
                           # metadata={"excluded_from_ui": True,
                                     # "file_editor": "plugins/jest/test_list.toml"})
    # package_json: str = field(default="plugins/jest/pacakge.json",
                              # metadata={"excluded_from_ui": True,
                                        # "file_editor": "plugins/jest/package.json"})
    eslintrc: str = field(default="plugins/jest/.eslintrc",
                          metadata={"excluded_from_ui": True,
                                    "file_editor": "plugins/jest/.eslintrc"})

