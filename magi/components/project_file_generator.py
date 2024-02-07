import os
import re


class ProjectFileGenerator:
    def __init__(self):
        pass


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
