from . import QA

def example_question_answer()->tuple:
    example_question = QA.generate_question()
    return example_question, QA.solve_question(example_question)


def generate_documentation():
    template = ""
    with open("modules/NetworkProjectEngine/document.md", "r") as f:
        template = f.read()
    from core.components.documentation import replace_template
    from . import config
    field_data = {
        "QUESTION_FORMAT": config.question_format
    }
    field_data["EXAMPLE_QUESTION"], field_data["EXAMPLE_ANSWER"] = example_question_answer()
    return replace_template(template, field_data)