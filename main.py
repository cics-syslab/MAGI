from core.managers.log_manager import LogManager
import sys
import argparse



# GUI will only be started for development purposes
def start_gui():
    from gui.app import start_app
    start_app()


def setup():
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--setup", action="store_true")
    parser.add_argument("-t","--test", action="store_true", help="Run self tests")
    parser.add_argument("-a","--autograder", action="store_true")
    parser.add_argument("-m","--mock", action="store_true")
    args = parser.parse_args()

    if args.setup:
        setup()
    elif args.test:
        pass
    elif args.autograder:
        from core.grader import grade_submission
        grade_submission()
    elif args.mock:
        pass
    else:
        start_gui()
        from core.managers.setting_manager import SettingManager
        SettingManager.save_settings()


if __name__ == '__main__':
    main()