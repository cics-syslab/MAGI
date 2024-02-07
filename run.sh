#!/bin/bash

# Get the current directory
current_dir="$(pwd)"

# Check if the current directory is already in PYTHONPATH
if [[ ":$PYTHONPATH:" != *":$current_dir:"* ]]; then
  # Add the current directory to PYTHONPATH for the current session
  export PYTHONPATH="$PYTHONPATH:$current_dir"
  echo "Added $current_dir to PYTHONPATH for the current session."
else
  echo "$current_dir is already in PYTHONPATH for the current session."
fi

# Run your Python script
python3 -m streamlit run webui/Hello.py 
