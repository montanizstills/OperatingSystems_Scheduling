import enum

from process import Process
from queue import Queue


class Algorithm:
    class ExecutionMode(enum.Enum):
        PREEMPTIVE = "PREEMPTIVE"
        NON_PREEMPTIVE = "NON_PREEMPTIVE"

    ALGORITHM_NAME: str

    def __init__(self, execution_mode: ExecutionMode):
        self.EXECUTION_MODE = execution_mode

    def get_execution_mode(self):
        return self.EXECUTION_MODE

    def run(self, queue: Queue, time_quantum: int):
        func = getattr(self, self.get_execution_mode().value.lower())
        if func.__name__ == 'preemptive':
            if time_quantum == -1:
                exit("Please specify a time quantum, negro.")
            func(queue, time_quantum)
        func(queue)

    def get_next_earliest_process(self, queue: Queue) -> Process:
        early: Process = min(queue.get_instance(), key=lambda process: process.arrival_time)
        print(f"next earliest process: {early.name}")
        return early

    def get_next_shortest_process(self, queue: Queue) -> Process:
        shortest: Process = min(queue.get_instance(), key=lambda process: process.service_time)
        print(f"next earliest process: {shortest.name}")
        return shortest


class FirstComeFirstServe(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "First-Come-First-Serve"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: Queue):
        """
        It is possible to implement a time quantum here, but it will achieve none.
        :param queue: The queue to exercise.
        :return: None
        """
        while len(queue.get_instance()) > 0:
            process_to_execute: Process = queue.pop_queue()
            process_to_execute.do_critical_section()

    def preemptive(self, queue: Queue, time_quantum: int = -1):
        if time_quantum == -1:
            exit("Please specify a time quantum.")
        process_to_execute: Process = queue.pop_queue()
        while process_to_execute.executed_time_during_turn != time_quantum:
            process_to_execute.do_critical_section()


class HighestResponseRatio(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "Highest-Response-Ratio-Next"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: Queue):
        pass

    def preemptive(self, queue: Queue):
        pass


class ShortestTimeRemaining(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "ShortestTimeRemaining"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: Queue):
        pass

    def preemptive(self, queue: Queue):
        pass


class MultilevelFeedback(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "Multilevel-Feedback"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: Queue):
        pass

    def preemptive(self, queue: Queue):
        pass


class RoundRobin(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "RoundRobin"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: Queue):
        pass

    def preemptive(self, queue: Queue):
        pass


class ShortestProcess(Algorithm):
    def __init__(self, execution_mode: Algorithm.ExecutionMode):
        self.ALGORITHM_NAME = "ShortestProcessNext"
        super().__init__(execution_mode)

    def non_preemptive(self, queue: Queue):
        pass

    def preemptive(self, queue: Queue):
        pass
