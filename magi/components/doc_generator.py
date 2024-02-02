import re


def replace_template(template: str, field_data: dict) -> str:
    """
    Replace the templates fields in the given templates string with the values in the given dictionary.

    : param templates: The templates string to replace the fields in.
    : param field_data: The dictionary containing the values to replace the fields with.
    : return: The templates string with the fields replaced.
    """

    result = re.search(r'\{_(.*?)_\}', template)
    replace_field = ''

    while result is not None:
        result = result.group()

        if result[2:-2] == replace_field:
            print('Dead loop')
            break

        replace_field = result[2:-2]

        if not replace_field:
            print('WARNING: Trivial \{__\} inside documentation. Removed')

        if result[2:-2] in globals() and callable(globals()[replace_field]):
            template = template.replace(result, globals()[replace_field]())

        elif replace_field in field_data or replace_field.lower() in field_data:
            if replace_field.lower() in field_data:
                replace_field = replace_field.lower()
            res = str(field_data[replace_field])
            if res != '0' and res != '':
                # print('Use ' + template_name+' directly from config')
                pass
            else:
                print('WARNING: Template ' + replace_field +
                      ' defined with a trivial value')
            template = template.replace(result, res)

        else:
            print('WARNING: Template ' + replace_field + ' not defined')
            template = template.replace(result, replace_field)

        result = re.search(r'\{_(.*?)_\}', template)

    return template
