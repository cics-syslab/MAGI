from dataclasses import dataclass
import os.path as op


@dataclass
class Directories:
    # /autograder
    autograder_root = op.join(r"C:\Users\kcc\OneDrive\Dev\gsgen", "assets/mock_autograder")
    # autograder_root + source
    src_path: str = r"C:\Users\kcc\OneDrive\Dev\gsgen"
    # Not needed
    template_dir = op.join(src_path, "assets/GRADESCOPE_TEMPLATE")
    
    core_dir = op.join(src_path, "core")

    project_files_dir = op.join(src_path, "project_files")

    submission_dir = op.join(autograder_root, "submission")


instance = Directories()