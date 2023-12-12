import collections
import threading

from algorithms.Algorithm import Algorithm


class CPU(threading.Thread):
    executing_time: float
    total_elapsed_time: float
    process_execution_start_time: float
    queue: collections.deque
    algorithm_execution_type: Algorithm

    def __init__(self):
        super().__init__()
        self.queue = collections.deque()
        self.interrupt_event = threading.Event()

    def run(self):
        while self.queue and not self.interrupt_event.is_set():
            print(f"CPU: Processing queue: `{self.queue.__str__()}` with scheduling algorithm: `{self.algorithm_execution_type.ALGORITHM_NAME}` as {self.algorithm_execution_type.EXECUTION_MODE.value}")
            while self.queue:
                self.algorithm_execution_type.run(self.queue)
