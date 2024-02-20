import os
import subprocess
import sys
import tqdm
from pathlib import Path



magi_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if magi_directory not in sys.path:
    sys.path.append(magi_directory)

app_path = Path(__file__).resolve().parent.parent


def check_directory():
    optional_dirs = ['logs', 'workdir', 'settings', 'modules', 'plugins']

    for d in optional_dirs:
        if not app_path.joinpath(d).exists():
            app_path.joinpath(d).mkdir()

    required_directories = ['magi']
    for d in required_directories:
        if not app_path.joinpath(d).exists():
            raise FileNotFoundError(f"Required directory {app_path.joinpath(d)} not found")


def check_addons_setup():
    all_setup_files = []
    for t in ['module', 'plugin']:
        if not app_path.joinpath(t + 's').exists():
            continue
        for addon in app_path.joinpath(t + 's').iterdir():
            if not addon.joinpath('setup.sh').exists():
                print(f"Addon {addon.name} is missing setup.sh, skipping")
                continue
            all_setup_files.append(addon.joinpath('setup.sh'))

    for setup_file in tqdm.tqdm(all_setup_files, desc="Running setup.sh"):
        subprocess.run(['sh', str(setup_file)], check=True)


def setup():
    check_directory()
    check_addons_setup()
    print("MAGI setup complete")


if __name__ == "__main__":
    setup()
