from dataclasses import dataclass, field
from typing import List


@dataclass
class ThreadState:
    id: int = 0
    succ_msg: str = "None"
    fail_msg: str = "None"
    draw_resource: List[int] = field(default_factory=list)
    release_resource: List[int] = field(default_factory=list)
    prerequisite: List[int] = field(default_factory=list)
    retry_window: int = 0
    final_state: bool = False
    succ_working_window: int = 0


@dataclass
class Resource:
    id: int = 0
    name: str = "None"
    limit: int = 0
    use_binary_semaphore: bool = False


@dataclass
class Config:
    thread_name: str = ""
    thread_func_name: str = ""
    thread_states: List[ThreadState] = field(default_factory=list)
    resources: List[Resource] = field(default_factory=list)
