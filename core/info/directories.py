import os.path as op
from dataclasses import dataclass


@dataclass
class Directories:
    import pathlib
    # autograder_root + source
    src_path: str = pathlib.Path(__file__).parent.parent.parent.resolve()
    
    template_dir = op.join(src_path, "assets/GRADESCOPE_TEMPLATE")

    core_dir = op.join(src_path, "core")
    project_files_dir = op.join(src_path, "project_files")
    logs_dir = op.join(src_path, "logs")
    # /autograder
    autograder_root = op.join(src_path, "assets/mock_autograder")
    if op.exists("/autograder"):
        autograder_root = "/autograder"
    
    submission_dir = op.join(autograder_root, "submission")
    result_path = op.join(autograder_root, "results/results.json")
instance = Directories()
