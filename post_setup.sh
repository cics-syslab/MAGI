#!/usr/bin/env bash

app_path=$(dirname "$(realpath "$0")")

check_addons_setup() {
    local all_setup_files=()
    for t in 'plugin' 'module'; do
        if [ ! -d "${app_path}/${t}s" ]; then
            continue
        fi
        for addon in "${app_path}/${t}s"/*; do
            if [ ! -d "${addon}" ]; then
                continue
            fi
            if [ ! -f "${addon}/setup.sh" ]; then
                echo "Addon $(basename "${addon}") is missing setup.sh, skipping"
                continue
            fi
            all_setup_files+=("${addon}/setup.sh")
        done
    done

    echo "Running setup.sh files..."
    echo "list: ${all_setup_files[@]}"
    for setup_file in "${all_setup_files[@]}"; do
        echo "Running ${setup_file}"
        sh "${setup_file}"
    done
}

chmod -R 777 workdir

apt-get update && apt-get install -y build-essential zip

check_addons_setup
echo "Add-ons setup complete"
