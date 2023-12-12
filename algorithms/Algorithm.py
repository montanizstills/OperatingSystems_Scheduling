import collections
import enum
import time

from process import Process


class Algorithm:
    class ExecutionMode(enum.Enum):
        PREEMPTIVE = "PREEMPTIVE"
        NON_PREEMPTIVE = "NON_PREEMPTIVE"

    ALGORITHM_NAME: str
    EXECUTION_MODE: ExecutionMode

    def __init__(self, execution_mode: ExecutionMode):
        self.EXECUTION_MODE = execution_mode

    def get_execution_mode(self):
        return self.EXECUTION_MODE

    def preemptive(self, queue: collections.deque):
        raise NotImplementedError

    def non_preemptive(self, queue: collections.deque):
        raise NotImplementedError

    def run(self, queue: collections.deque):
        # get the attribute defined in param 2, return the function, then immeidately execute
        getattr(self, self.get_execution_mode().value.lower())(queue)

    def get_next_earliest_process(self, queue: collections.deque) -> Process:
        early: Process = min(queue, key=lambda process: process.arrival_time)
        print(f"next earliest process: {early.name}")
        return early

    def get_next_shortest_process(self, queue: collections.deque) -> Process:
        shortest: Process = min(queue, key=lambda process: process.service_time)
        print(f"next earliest process: {shortest.name}")
        return shortest

    def execute_process(self, process: Process) -> None:
        for _i in range(1, process.service_time + 1):
            print(f"executing process {process.name}...")
            time.sleep(1)
            print(f"Elapsed time {_i}")


class FirstComeFirstServe(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "First-Come-First-Serve"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")

    def preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")


class HighestResponseRatio(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "Highest-Response-Ratio-Next"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")

    def preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")


class ShortestTimeRemaining(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "ShortestTimeRemaining"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")

    def preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")


class MultilevelFeedback(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "Multilevel-Feedback"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")

    def preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")


class RoundRobin(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "RoundRobin"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")

    def preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")


class ShortestProcess(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "ShortestProcessNext"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")

    def preemptive(self, queue: collections.deque):
        print(f"executing {self.ALGORITHM_NAME} with options: {self.EXECUTION_MODE}")
