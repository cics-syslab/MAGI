#!/bin/sh
apt-get update && apt-get install -y npm node || { echo "Error installing libgtest-dev and cmake"; exit 1; }
