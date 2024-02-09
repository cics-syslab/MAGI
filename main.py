import argparse
from pathlib import Path


def setup():
    required_dirs = ['logs', 'workdir', 'settings', 'modules', 'plugins']
    app_path = Path(__file__).resolve().parent
    for d in required_dirs:
        if not app_path.joinpath(d).exists():
            app_path.joinpath(d).mkdir()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--setup", action="store_true")
    parser.add_argument("-t", "--test", action="store_true", help="Run self tests")
    parser.add_argument("-a", "--autograder", action="store_true")
    parser.add_argument("-m", "--mock", action="store_true")
    args = parser.parse_args()

    if args.setup:
        setup()
        return
    import logging
    from logging import handlers
    import time

    log_format = '%(asctime)s - %(name)s - %(levelname)s: %(message)s - %(pathname)s[line:%(lineno)d]'
    logging.basicConfig(format=log_format, level=logging.DEBUG)
    # TODO: log file path should be configured
    th = handlers.TimedRotatingFileHandler(filename=f"logs/log-{time.strftime('%m%d%H%M')}.txt", encoding='utf-8')
    formatter = logging.Formatter(log_format)
    th.setFormatter(formatter)
    logging.getLogger().addHandler(th)

    if args.autograder:
        from magi.components.grader import grade_submission
        grade_submission()


if __name__ == '__main__':
    main()
