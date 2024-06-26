import os
import sys
from pathlib import Path

magi_path = Path(__file__).resolve().parent.parent

if magi_path not in sys.path:
    sys.path.append(str(magi_path))
    
from magi.utils.render import render_templates


# Function to create addon structure
def create_addon(addon_type, addon_name):
    base_path = os.path.join(os.getcwd(), addon_type + 's', addon_name)
    try:
        # Create the base directory for the addon
        os.makedirs(base_path)
        render_templates(os.path.join(magi_path, 'static', 'ADDON_TEMPLATE'), {
            'addon_type': addon_type,
            'addon_name': addon_name,
        }, base_path)

    except Exception as e:
        print(f"Error creating addon structure: {e}")


# Main function to run the script
def main():
    print("Initialize your MAGI addon development.")
    addon_type = input("Enter the addon type (module/plugin): ").strip().lower()
    if addon_type not in ['module', 'plugin']:
        print("Invalid addon type. Please enter 'module' or 'plugin'.")
        return

    addon_name = input("Enter the addon name: ").strip()
    if not addon_name:
        print("Addon name cannot be empty.")
        return
    # check if the addon name is already taken
    for t in ['module', 'plugin']:

        addon_path = os.path.join(os.getcwd(), t + 's', addon_name)
        if os.path.exists(addon_path):
            print(f"Addon with the name {addon_name} already exists.")
            return

    create_addon(addon_type, addon_name)
    print(f"Addon {addon_name} created successfully.")
    print("Please refer to the documentation for further steps.")
    print("Happy coding!")


if __name__ == "__main__":
    main()
