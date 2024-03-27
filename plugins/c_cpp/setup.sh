#!/bin/sh

setup_gtest() {
    # Install libgtest-dev and cmake
    apt-get update && apt-get install -y build-essential libgtest-dev cmake || { echo "Error installing libgtest-dev and cmake"; exit 1; }

    # Go to the gtest source directory and build gtest
    cd /usr/src/gtest || { echo "Error navigating to /usr/src/gtest"; exit 1; }
    cmake CMakeLists.txt && make || { echo "Error building gtest"; exit 1; }

    for file in *.a; do
        if [ -e "$file" ]; then
            cp "$file" /usr/lib || { echo "Error copying .a files to /usr/lib"; exit 1; }
        fi
    done
}


setup_gtest
