import os
import shutil

import jinja2

from magi.common.addon import hookimpl
from .config import Config
from .grader import grade

env = jinja2.Environment(loader=jinja2.FileSystemLoader('modules/ClientServerSocket/templates'))


class ClientServerSocket:
    def __init__(self):
        self.config = Config
        print("ClientServerSocket init")

    @hookimpl
    def generate(self):
        # use jinja to render the solution file
        template = env.get_template('client.c.jinja')
        output = template.render(magic_str=Config.magic_str)
        from magi.managers import InfoManager
        with open(InfoManager.Directories.OUTPUT_DIR / "solution" / "client.c", "w+") as f:
            f.write(output)
        shutil.copyfile("modules/ClientServerSocket/QA.py", InfoManager.Directories.OUTPUT_DIR / "solution" / "QA.py")
        os.makedirs(InfoManager.Directories.OUTPUT_DIR / "misc" / "server", exist_ok=True)
        shutil.copyfile("modules/ClientServerSocket/QA.py",
                        InfoManager.Directories.OUTPUT_DIR / "misc" / "server" / "QA.py")
        shutil.copyfile("modules/ClientServerSocket/server.py",
                        InfoManager.Directories.OUTPUT_DIR / "misc" / "server" / "server.py")
        template = env.get_template('run.sh.jinja')
        output = template.render(magic_str=Config.magic_str)
        with open(InfoManager.Directories.OUTPUT_DIR / "misc" / "server" / "run.sh", "w+") as f:
            f.write(output)

    @hookimpl
    def generate_documentation(self):
        template = env.get_template('documentation.md.jinja')
        from .config import Config
        import subprocess
        import sys
        from magi.managers import SettingManager
        sample_question = subprocess.run([sys.executable, "-m", "QA.py"], cwd="modules/ClientServerSocket",
                                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                         text=True).stdout
        sample_question = sample_question
        sample_answer = subprocess.run([sys.executable, "-m", "QA.py", sample_question],
                                       cwd="modules/ClientServerSocket", stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True).stdout
        doc = template.render(sample_question=sample_question, sample_answer=sample_answer, magic_str=Config.magic_str,
                              question_format=Config.question_format,
                              project_name=SettingManager.BaseSettings.project_name)
        return doc

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
