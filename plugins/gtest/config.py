from dataclasses import dataclass

@dataclass
class Config:
    test_executable: str = "test"
    test_list_file: str = "test_list.yaml"



    
@dataclass
class TestCase:
    # number: Optional[str]
    score: float = 0
    max_score: float = 0
    visibility: str = Visibility.after_published
    output: str = ""
    name: str = ""
    status: str = ""

    # tags: list = field(default_factory=list)
    # extra_data:str = ""

    def fail_test(self, msg: str):
        self.output += "\n" + msg
        self.score = 0
        self.status = "failed"

    def pass_test(self, msg: str):
        self.output += "\n" + msg
        self.score = self.max_score
        self.status = "passed"

    def add_output_msg(self, msg: str):
        self.output += "\n" + msg