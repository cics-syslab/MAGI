from magi.managers import AddonManager


def setup_grader():
    AddonManager.setup()
    pass


def setup_dev():
    setup_grader()
    pass


if __name__ == "__main__":
    setup_dev()
