#!/usr/bin/env bash

app_path=$(dirname "$(dirname "$(realpath "$0")")")
check_directory() {
    local optional_dirs=('logs' 'workdir' 'settings' 'modules' 'plugins')

    for d in "${optional_dirs[@]}"; do
        if [ ! -d "${app_path}/${d}" ]; then
            mkdir -p "${app_path}/${d}"
        fi
    done

    local required_directories=('magi')

    for d in "${required_directories[@]}"; do
        if [ ! -d "${app_path}/${d}" ]; then
            echo "Required directory ${app_path}/${d} not found" >&2
            exit 1
        fi
    done
}

check_addons_setup() {
    local all_setup_files=()
    for t in 'module' 'plugin'; do
        if [ ! -d "${app_path}/${t}s" ]; then
            continue
        fi
        for addon in "${app_path}/${t}s"/*; do
            if [ ! -f "${addon}/setup.sh" ]; then
                echo "Addon $(basename "${addon}") is missing setup.sh, skipping"
                continue
            fi
            all_setup_files+=("${addon}/setup.sh")
        done
    done

    echo "Running setup.sh files..."
    for setup_file in "${all_setup_files[@]}"; do
        sh "${setup_file}"
    done
}

check_directory
check_addons_setup
echo "MAGI setup complete"
