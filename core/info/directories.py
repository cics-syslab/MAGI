import os.path as op
from dataclasses import dataclass


@dataclass
class Directories:
    import pathlib

    # /autograder
    autograder_root = op.join(r"C:\Users\kcc\OneDrive\Dev\gsgen", "assets/mock_autograder")
    if op.exists("/autograder"):
        autograder_root = "/autograder"
    
    # autograder_root + source
    src_path: str = pathlib.Path(__file__).parent.parent.parent.resolve()
    
    template_dir = op.join(src_path, "assets/GRADESCOPE_TEMPLATE")

    core_dir = op.join(src_path, "core")

    project_files_dir = op.join(src_path, "project_files")

    submission_dir = op.join(autograder_root, "submission")


instance = Directories()
