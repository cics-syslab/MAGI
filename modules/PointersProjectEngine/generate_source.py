import os
import re
import sys

from jinja2 import Environment, FileSystemLoader
from magi._private.hookspecs import hookimpl

from .config import Config


@hookimpl
def generating():
    from magi.components.render import render_templates
    from magi.info import Directories
    render_templates(
        os.path.join(Directories.SRC_PATH, "modules", "PointersProjectEngine", "template"),
        Config.__dict__,
        os.path.join(Directories.WORK_DIR)
    )


def convert_template(template_content):
    # Replace template variables in the form {_VAR_} for Jinja double bracket reading
    pattern = re.compile(r'\{_(\w+)_\}')
    converted_template = re.sub(pattern, r'{{ \1 }}', template_content)
    return converted_template


def generate_code(template_file, output_file, variables):
    # Set up Jinja environment
    env = Environment(loader=FileSystemLoader("."))  # Assuming the template is in the same directory
    # Load the template
    with open(template_file, "r") as template_file:
        template_content = template_file.read()
    converted_template = convert_template(template_content)

    # Rendering the transformed template file using Jinja
    template = env.from_string(converted_template)
    rendered_code = template.render(variables)
    with open(output_file, "w") as file:
        file.write(rendered_code)
    print(f"{output_file} generated successfully.")


if __name__ == "__main__":
    # Get variables from Config class
    variables = {
        "PROJECT_NAME": Config.project_name,
        "DESCRIPTOR1": Config.descriptor_1,
        "DESCRIPTOR2": Config.descriptor_2,
        "ITEM1": Config.item_1,
        "ITEM2": Config.item_2,
        "ITEM3": Config.item_3,
        "CONTAINER": Config.container_name,
        "CONTAINER_TYPE": Config.container_type,
        "ITEM": Config.item_type,
        "CONTAINER_NAME_LENGTH": str(len(Config.container_name) + 1),  # +1 to account for null terminator
    }

    # Check if template file is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python generate_source.py <template_file>")
        sys.exit(1)
    # Get the template file from the command-line argument
    template_file = sys.argv[1]
    output_file = f"generated_{os.path.basename(template_file)}"
    generate_code(template_file, output_file, variables)
