#!/usr/bin/env bash

apt-get update
apt-get install -y build-essential python3 python3-setuptools python3-dev zip libgtest-dev cmake
apt update
apt install -y python3-pip
pip3 install PyYAML

cd /usr/src/gtest && cmake CMakeLists.txt && make && cp *.a /usr/lib

# Install python
apt-get install -y python python3 python3.7 python3-pip python3-dev jq
# Upgrade pip
python3.7 -m pip install -U --force-reinstall pip
# Install gspack dependencies
python3.7 -m pip install subprocess32 numpy scipy matplotlib
# Install solution script dependencies
if [[ -f "/autograder/source/requirements.txt" ]]; then
    python3.7 -m pip install -r /autograder/source/requirements.txt
fi



python3 core/initializer.py
