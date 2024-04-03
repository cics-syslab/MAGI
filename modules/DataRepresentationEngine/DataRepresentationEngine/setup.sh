#!/usr/bin/env bash

apt-get update
apt-get install -y build-essential python3 python3-setuptools python3-dev zip libgtest-dev cmake
apt update
apt install -y python3-pip
pip3 install PyYAML

cd /usr/src/gtest && cmake CMakeLists.txt && make && cp *.a /usr/lib
