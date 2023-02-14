from .managers import AddonManager
from .components import handle_submission


def grade_submission():
    handle_submission.remove_existing_submission_files()
    missing_file = handle_submission.check_submitted_files()
    if missing_file:
        AddonManager.fail_all(f"Missing file(s): {', '.join(missing_file)}")
        return
    handle_submission.move_submission_files()
    AddonManager.grade()
    from .output import output_result
    output_result()

if __name__ == "__main__":
    grade_submission()
