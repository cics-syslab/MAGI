import logging
import os
import re

import jinja2


def render_template(template_path, context, output_path=None, ):
    """
    Renders a template file using Jinja2 and writes the result to an output file.

    :param template_path: The path to the template file
    :param context: The context to render the template with
    :param output_path: The path to the output file
    """
    if not output_path:
        output_path = template_path[:-6]
    with open(template_path) as f:
        template = jinja2.Template(f.read())
        result = template.render(context)
        with open(output_path, 'w') as f:
            f.write(result)

    return output_path


def render_templates(template_dir, context, output_dir=None, exclude=None, preserve_relative_path=True):
    """
    Renders all template files in a directory using Jinja2 and writes the result to an output directory.

    :param template_dir: The path to the template directory
    :param context: The context to render the template with
    :param output_dir: The path to the output directory
    :param exclude: A list of files to exclude from rendering
    :param preserve_relative_path: Whether to preserve the relative path of the template files in the output directory
    """
    if not output_dir:
        output_dir = template_dir

    for dirpath, dirnames, filenames in os.walk(template_dir):

        rel_dirpath = os.path.relpath(dirpath, template_dir)
        for filename in filenames:
            if exclude and filename in exclude:
                continue
            if filename.endswith('.jinja'):
                template_path = os.path.join(dirpath, filename)
                if not preserve_relative_path:
                    output_path = os.path.join(output_dir, filename[:-6])
                else:
                    output_path = os.path.join(output_dir, rel_dirpath, filename[:-6])
                if not os.path.exists(os.path.dirname(output_path)):
                    os.makedirs(os.path.dirname(output_path))

                logging.info(f'Rendering {template_path} to {output_path}')
                render_template(template_path, context, output_path)

    return output_dir


PRIVATE = "private"
PUBLIC = "public"
BLOCK_TYPES = [PRIVATE, PUBLIC]
REGEX_PATTERNS = {
    PRIVATE: {
        "start": re.compile(r".*(//|#).*PRIVATE_BEGIN.*"),
        "end": re.compile(r".*(//|#).*PRIVATE_END.*")
    },
    PUBLIC: {
        "start": re.compile(r".*/\* PUBLIC_BEGIN.*"),
        "end": re.compile(r".*PUBLIC_END.*\*/.*")
    }
}


def process_distribution_version(input_str, version, keep_public=True) -> str:
    if version not in BLOCK_TYPES:
        raise ValueError("version_type should be either 'public' or 'private'.")

    # Determine which version to remove
    removal_version = PRIVATE if version == PUBLIC else PUBLIC

    block_stack = []  # A stack to manage nested blocks
    lines = input_str.splitlines()
    processed_lines = []

    for line in lines:
        # Check if we're inside a block
        if block_stack:
            if REGEX_PATTERNS[block_stack[-1]]["end"].match(line):
                block_stack.pop()
                processed_lines.append("")
                continue

        is_start_tag = False
        # Check for start tags
        for block_type in BLOCK_TYPES:
            if REGEX_PATTERNS[block_type]["start"].match(line):
                block_stack.append(block_type)
                processed_lines.append("")
                is_start_tag = True
                break
        if is_start_tag:
            continue

        # If we're inside the removal block and not keeping public when version is private, skip adding
        if block_stack and block_stack[-1] == removal_version and not (version == PRIVATE and keep_public):
            continue

        processed_lines.append(line)

    # Check if there are unmatched blocks
    if block_stack:
        unmatched_blocks = ", ".join(block_stack)
        raise ValueError(f"Unmatched blocks detected: {unmatched_blocks}")

    return "\n".join(processed_lines)


def generate_distribution_version(file_path, output_file_path, version, keep_public=True):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    with open(file_path, 'r') as f:
        input_str = f.read()

    processed_str = process_distribution_version(input_str, version, keep_public)

    # Ensure the directory of the output file exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, 'w') as out_f:
        out_f.write(processed_str)
