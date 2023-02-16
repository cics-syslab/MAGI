def generate_documentation(file_path:str):
    from core.managers import AddonManager
    from core.managers import SettingManager
    docs = AddonManager.generate_documentation()

    if not docs:
        return

    doc_string = f"# {SettingManager.BaseSettings.project_name} \n {SettingManager.BaseSettings.project_desc} \n"

    doc_string+="\n".join(docs)
    with open(file_path, "w+") as f:
        f.write(doc_string)

def replace_template(template:str, field_data:dict):
    import re
    result = re.search(r'\{_(.*?)_\}', template)
    replace_field = ''

    while result is not None:
        result = result.group()

        if (result[2:-2] == replace_field):
            print('Dead loop')
            break

        replace_field = result[2:-2]

        if not replace_field:
            print('WARNING: Trival \{__\} inside documentation. Removed')

        if result[2:-2] in globals() and callable(globals()[replace_field]):
            template = template.replace(result, globals()[replace_field]())

        elif replace_field in field_data or replace_field.lower() in field_data:
            if replace_field.lower() in field_data:
                replace_field = replace_field.lower()
            res = str(field_data[replace_field])
            if res != '0' and res != '':
                #print('Use ' + template_name+' directly from config')
                pass
            else:
                print('WARNING: Template ' + replace_field +
                      ' defined with a trival value')
            template = template.replace(result, res)

        else:
            print('WARNING: Template ' + replace_field+' not defined')
            template = template.replace(result, replace_field)

        result = re.search(r'\{_(.*?)_\}', template)
    
    return template