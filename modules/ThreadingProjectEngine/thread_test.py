import datetime
import re
from subprocess import Popen, PIPE

from . import config
from .project_config import ThreadState

min_resource_limit = float('inf')


def get_thread_state_by_id(thread_state_id: int) -> ThreadState:
    for state in config.thread_states:
        if state.id == thread_state_id:
            return state
    return None


class Msg:
    def __init__(self, msg_str: str) -> None:
        self.thread_id = -1
        self.state = -1
        self.msg_type = -1

        for state in config.thread_states:
            state_msg = [state.fail_msg.split(), state.succ_msg.split()]
            for msg_type in [0, 1]:
                if len(state_msg[msg_type]) != len(msg_str.split()):
                    continue

                match = True
                thread_id = -1
                for idx, chunk in enumerate(msg_str.split()):
                    if chunk != state_msg[msg_type][idx]:
                        if state_msg[msg_type][idx] == '{THREAD_ID}':
                            try:
                                thread_id = int(
                                    re.search('\d+', chunk).group()) - 1
                            except:
                                match = False
                        else:
                            match = False
                            break
                if match:
                    self.thread_id = thread_id
                    self.state = state.id
                    self.msg_type = msg_type
                    return

        print('The line {', msg_str, '}cannot be recognized, check the format')


class ResourceRecord:
    def __init__(self, json_dict=(), **kwargs) -> None:
        self.id = 0
        self.name = ''
        self.limit = 0
        self.usage = 0
        self.peek_usage = 0
        self.below_zero = False
        self.__dict__.update(json_dict, **kwargs)

        global min_resource_limit

        fail_detectable = False
        for state in config.thread_states:
            if self.id in state.draw_resource and state.fail_msg:
                fail_detectable = True
                break

        if min_resource_limit > self.limit > 0 and fail_detectable:
            min_resource_limit = self.limit

    def draw(self, count: int = 1) -> None:
        self.usage += 1
        self.peek_usage = max(self.usage, self.peek_usage)

    def release(self, count: int = 1) -> None:
        self.usage -= 1
        if self.usage < 0 and self.limit > 0:
            self.below_zero = True

    def is_overflow(self):
        return self.peek_usage > self.limit > 0

    def is_underflow(self):
        return self.below_zero

    def reached_limit(self):
        return self.peek_usage >= self.limit > 0


resource_records = []


def get_resource_by_id(resource_id: int) -> ResourceRecord:
    global resource_records
    for resource_record in resource_records:
        if resource_record.id == resource_id:
            return resource_record
    return None


class ThreadRecord:
    def __init__(self, thread_id) -> None:
        self.thread_id = thread_id
        self.state_trace = []
        self.num_success = 0
        self.num_failed = 0
        self.state = -1
        self.skip_state = False
        self.revisit_state = False
        self.next_retry_time = None
        self.exceed_retry_window = False

    def go_state(self, state: ThreadState, msg_type: int) -> None:
        if self.next_retry_time is not None:
            if datetime.datetime.now() > self.next_retry_time:
                self.exceed_retry_window = True
            else:
                self.next_retry_time = None

        if state.id in self.state_trace:
            self.revisit_state = True

        for prerequisite in state.prerequisite:
            if prerequisite not in self.state_trace:
                self.skip_state = True

        if msg_type == 0:
            self.num_failed += 1
            if state.retry_window > 0:
                self.next_retry_time = datetime.datetime.now(
                ) + 2 * datetime.timedelta(seconds=state.retry_window)
        elif msg_type == 1:
            self.num_success += 1
            self.state_trace.append(state.id)
            self.state = state.id

            for resource_id in state.draw_resource:
                get_resource_by_id(resource_id).draw()
            for resource_id in state.release_resource:
                get_resource_by_id(resource_id).release()


def true_or_error_msg(result: bool, comment: str) -> tuple:
    if result:
        return True, ''
    else:
        return False, comment


class ThreadTest:
    def update_from_msg(self, msg: Msg) -> None:
        if msg is None:
            return
        thread_record = self.thread_records[msg.thread_id]
        thread_record.go_state(get_thread_state_by_id(msg.state), msg.msg_type)

    # TODO: In case of not recognizing the message, the student should see it
    def run(self):
        msg_order = []
        self.thread_records = []
        for thread_id in range(self.thread_num):
            self.thread_records.append(ThreadRecord(thread_id))

        global resource_records
        resource_records = []
        for resource in config.config_json['resource']:
            resource_records.append(ResourceRecord(resource))

        from magi.info.directories import Directories
        exec_name = config.exec_name
        # TODO: Check return code so we could know the program has some problem(in case no output)
        # so the pipe will read in real-time instead of all lines at once
        unbuffered = ["stdbuf", "-i0", "-o0", "-e0"]
        p = Popen(unbuffered + [exec_name, str(self.thread_num)], bufsize=0, stdout=PIPE,
                  universal_newlines=True, cwd=Directories.WORK_DIR)

        # This probably works with Python3.10+
        # p = Popen([exec_name, str(self.thread_num)], bufsize=0,stdout=PIPE,universal_newlines=True,pipesize =0)

        while p.poll() is None:
            output = p.stdout.readline()
            if (len(output.rstrip()) == 0):
                continue
            msg = Msg(output.rstrip())
            self.update_from_msg(msg)
            msg_order.append(msg.thread_id)
            msg_order.append(msg.state)
            msg_order.append(msg.msg_type)
        self.msg_orders.append(msg_order)
        self.init = True

    def __init__(self, thread_num=1):
        self.thread_num = thread_num
        self.init = False
        self.thread_records = []
        self.msg_orders = []
        self.run()

    def test_all_thread_is_final(self) -> tuple:
        failed_threads = []
        for i in range(self.thread_num):
            # not presented
            if self.thread_records[i].state == -1:
                failed_threads.append(i)
                continue

            if not get_thread_state_by_id(self.thread_records[i].state).final_state:
                failed_threads.append(i)

        return true_or_error_msg(len(failed_threads) == 0, str(len(failed_threads)) + " thread(s) are not finished.")

    def test_all_thread_presented(self) -> tuple:
        absent_threads = []
        for i in range(self.thread_num):
            if (self.thread_records[i].num_success == 0) & (self.thread_records[i].num_failed == 0):
                absent_threads.append(i)

        return true_or_error_msg(len(absent_threads) == 0, str(len(
            absent_threads)) + " thread(s) never show up, check race condition when assign id.")

    def test_all_thread_blocked_once(self) -> tuple:
        direct_passed_threads = []
        for i in range(self.thread_num):
            if (self.thread_records[i].num_failed == 0):
                direct_passed_threads.append(i)

        global min_resource_limit
        # TODO: change the min_resource_limit to the resource's peak usage, so who got overflow error wont also get this failed
        num_thread_exceed_limit = len(direct_passed_threads) - min_resource_limit

        return true_or_error_msg(num_thread_exceed_limit <= 0,
                                 str(num_thread_exceed_limit) + ' more thread(s) never got blocked.')

    def test_all_thread_not_skip_state(self) -> tuple:
        thread_skip_state = []
        for i in range(self.thread_num):
            if (self.thread_records[i].skip_state):
                thread_skip_state.append(i)
        return true_or_error_msg(len(thread_skip_state) == 0,
                                 str(len(thread_skip_state)) + " thread(s) skiped one or more states.")

    def test_all_thread_not_revisit_state(self) -> tuple:
        thread_revisit_state = []
        for i in range(self.thread_num):
            if (self.thread_records[i].revisit_state):
                thread_revisit_state.append(i)
        return true_or_error_msg(len(thread_revisit_state) == 0,
                                 str(len(thread_revisit_state)) + " thread(s) revisited one or more states.")

    # no lock on wait
    def test_all_failure_retried_on_time(self) -> tuple:
        thread_lazy = []
        for i in range(self.thread_num):
            if (self.thread_records[i].exceed_retry_window):
                thread_lazy.append(i)
        return true_or_error_msg(len(thread_lazy) == 0, str(len(
            thread_lazy)) + " thread(s) didn't retry on time, maybe wait() is included in semaphore.")

    def test_all_resource_filled(self) -> tuple:
        unfilled_resources = []
        global resource_records
        for resource in resource_records:
            if not resource.reached_limit():
                unfilled_resources.append(resource.id)

        return true_or_error_msg(len(unfilled_resources) == 0,
                                 str(len(unfilled_resources)) + ' resource(s) are not well used.')

    def test_all_resource_not_overflow(self) -> tuple:
        overflow_resources = []
        global resource_records
        for resource in resource_records:
            if resource.is_overflow():
                overflow_resources.append(resource.id)

        return true_or_error_msg(len(overflow_resources) == 0,
                                 str(len(overflow_resources)) + ' resource(s) got overflowed.')

    def test_all_resource_not_underflow(self) -> tuple:
        underflow_resources = []
        global resource_records
        for resource in resource_records:
            if resource.is_underflow():
                underflow_resources.append(resource.id)

        return true_or_error_msg(len(underflow_resources) == 0,
                                 str(len(underflow_resources)) + ' resource(s) got underflowed.')

    def test_order_not_fixed(self) -> tuple:
        num_iteration = 3
        for _ in range(num_iteration - 1):
            self.run()
        all_same = True
        for i in range(num_iteration - 1):
            all_same &= (self.msg_orders[i] == self.msg_orders[i + 1])

        return true_or_error_msg(not all_same, "Fixed Schedule Deteched")


if __name__ == '__main__':
    pass
