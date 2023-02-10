#!/usr/bin/env bash
# This script is run by the autograder to set up the environment for the
# autograder. It is run before the autograder starts, and before the student's
# code is run.

ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime
apt-get update
# Install python
apt-get install -y python3.8 python3-pip python3-dev python3-setuptools jq zip
# Upgrade pip
python3.8 -m pip install -U --force-reinstall pip

apt-get install libgtest-dev cmake
cd /usr/src/gtest && cmake CMakeLists.txt && make && cp *.a /usr/lib
python3.8 -m pip install PyYAML
# Install solution script dependencies
if [[ -f "/autograder/source/requirements.txt" ]]; then
    python3.8 -m pip install -r /autograder/source/requirements.txt
fi