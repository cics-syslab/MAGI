import argparse
import logging
import time
from logging import handlers


# GUI will only be started for development purposes
def start_gui():
    from gui.app import start_app
    start_app()


def setup():
    pass


def main():
    log_format = '%(asctime)s - %(name)s - %(levelname)s: %(message)s - %(pathname)s[line:%(lineno)d]'
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    # TODO: log file path should be configured
    th = handlers.TimedRotatingFileHandler(filename=f"logs/log-{time.strftime('%m%d%H%M')}.txt", encoding='utf-8')
    formatter = logging.Formatter(log_format)
    th.setFormatter(formatter)
    logging.getLogger().addHandler(th)

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--setup", action="store_true")
    parser.add_argument("-t", "--test", action="store_true", help="Run self tests")
    parser.add_argument("-a", "--autograder", action="store_true")
    parser.add_argument("-m", "--mock", action="store_true")
    args = parser.parse_args()

    if args.setup:
        setup()
    elif args.test:
        pass
    elif args.autograder:
        from magi.components.grader import grade_submission
        grade_submission()
    elif args.mock:
        pass
    else:
        start_gui()
        from magi.managers import SettingManager
        SettingManager.save_settings()


if __name__ == '__main__':
    main()
