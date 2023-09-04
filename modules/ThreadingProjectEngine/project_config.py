from dataclasses import dataclass, field
from typing import List, Optional


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
class ThreadTestCase:
    name: Optional[str]
    thread_num: int = 1
    max_score: int = 10
    visibility: str = "visible"
    methods: List[str] = field(default_factory=list, metadata={"options": [
        "test_all_thread_is_final",
        "test_all_thread_presented",
        "test_all_resource_not_underflow",
        "test_all_resource_not_overflow",
        "test_all_resource_filled",
        "test_all_failure_retried_on_time",
        "test_all_thread_not_revisit_state",
        "test_all_thread_not_skip_state",
        "test_all_thread_blocked_once",
        "test_order_not_fixed"]})


@dataclass
class ProjectConfig:
    exec_name: str = "app"
    thread_name: str = ""
    thread_func_name: str = ""
    thread_states: List[ThreadState] = field(default_factory=list)
    resources: List[Resource] = field(default_factory=list)
    tests: List[ThreadTestCase] = field(default_factory=list)
