import sys
from pathlib import Path

magi_path = Path(__file__).resolve().parent.parent

if magi_path not in sys.path:
    sys.path.append(str(magi_path))

def check_directory():
    optional_dirs = ['logs', 'workdir', 'settings', 'modules', 'plugins', 'output']

    for d in optional_dirs:
        if not magi_path.joinpath(d).exists():
            magi_path.joinpath(d).mkdir()

    required_directories = ['magi']
    for d in required_directories:
        if not magi_path.joinpath(d).exists():
            raise FileNotFoundError(f"Required directory {magi_path.joinpath(d)} not found")


def setup():
    check_directory()


if __name__ == "__main__":
    setup()
