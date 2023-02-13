from .managers import ModuleManager
from .components import handle_submission


def grade():
    handle_submission.remove_existing_submission_files()
    handle_submission.check_submitted_files()
    handle_submission.move_submission_files()
    ModuleManager.grade()


if __name__ == "__main__":
    grade()
