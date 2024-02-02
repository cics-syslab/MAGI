import jinja2
import os
import logging


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
