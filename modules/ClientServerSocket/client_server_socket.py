from magi.common.addon import hookimpl
from .config import Config
from .gen_doc import generate_documentation
from .grader import grade
import jinja2


class ClientServerSocket:
    def __init__(self):
        self.config = Config
        print("ClientServerSocket init")

    @hookimpl
    def generate(self):
        # use jinja to render the solution file
        env = jinja2.Environment(loader=jinja2.FileSystemLoader('modules/ClientServerSocket/templates'))
        template = env.get_template('client.c')
        output = template.render()
        from magi.managers import InfoManager
        with open(InfoManager.Directories.OUTPUT_DIR / "solution" / "client.c", "w+") as f:
            f.write(output)

    @hookimpl
    def generate_documentation(self):
        return generate_documentation()

    @hookimpl
    def grade(self):
        grade()

    def webui(self):
        # import importlib
        pass
        # # importlib.reload(QA)
        # sample_question = QA.generate_question()
        # sample_answer = QA.solve_question(sample_question)
        # get the question by pipe instead of import
        # import subprocess
        # import sys
        # sample_question = subprocess.run([sys.executable, "-m", "QA.py"], cwd= "modules/ClientServerSocket",stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        # sample_question = sample_question.rea
        # sample_answer = subprocess.run([sys.executable, "-m", "QA.py", sample_question], cwd= "modules/ClientServerSocket",stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        # st.write(f"sample question: {sample_question}")
        # st.write(f"answer: {sample_answer}")
