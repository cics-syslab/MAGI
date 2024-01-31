from core.common.addon import hookimpl
from .config import Config
from .gen_doc import generate_documentation
from .grader import grade


class NetworkProjectEngine:
    def __init__(self):
        self.config = Config
        print("NetworkProjectEngine init")

    @hookimpl
    def generate_documentation(self):
        generate_documentation()

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
        # sample_question = subprocess.run([sys.executable, "-m", "QA.py"], cwd= "modules/NetworkProjectEngine",stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        # sample_question = sample_question.rea
        # sample_answer = subprocess.run([sys.executable, "-m", "QA.py", sample_question], cwd= "modules/NetworkProjectEngine",stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout
        # st.write(f"sample question: {sample_question}")
        # st.write(f"answer: {sample_answer}")
