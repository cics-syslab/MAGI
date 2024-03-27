#!/usr/bin/env bash
# This script is run by the autograder to set up the environment for the
# autograder. It is run before the autograder starts, and before the student's
# code is run.

# update the system timezone
ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

apt-get update

check_and_set_python() {
    if command -v python3.10 &> /dev/null; then
        echo "Python 3.10 is installed."
        update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1
    elif command -v python3.8 &> /dev/null; then
        echo "Python 3.8 is installed."
        update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
    else
        echo "Neither Python 3.8 nor Python 3.10 is installed. Make sure you are using the correct image (Ubuntu 20.04 or 22.04)."
        exit 1
    fi
}

check_and_set_python

useradd -ms /bin/bash student
chmod -R u-r /autograder

# Install MAGI dependencies
if [[ -f "/autograder/source/requirements.txt" ]]; then
    pip install -r /autograder/source/requirements.txt
else
    echo "No requirements.txt file found."
    exit 1
fi

cd /autograder/source
./setup.sh
python3 scripts/setup.py
