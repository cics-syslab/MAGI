#!/bin/sh
apt-get update && apt-get install -y npm node || { echo "Error installing npm and node"; exit 1; }
