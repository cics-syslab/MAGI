from . import QA


def example_question_answer() -> tuple:
    example_question = QA.generate_question()
    return example_question, QA.solve_question(example_question)


def generate_documentation():
    template: str = ""
    with open("modules/ClientServerSocket/document.md", "r", encoding="utf-8") as f:
        template = f.read()
    from magi.components.doc_generator import replace_template
    from . import Config
    example_question, example_answer = example_question_answer()
    field_data = {"QUESTION_FORMAT": Config.question_format,
                  "EXAMPLE_QUESTION": example_question,
                  "EXAMPLE_ANSWER": example_answer}
    return replace_template(template, field_data)
