import threading

from algorithm import Algorithm
from queue import Queue


class CPU(threading.Thread):
    executing_time: float
    total_elapsed_time: float
    process_execution_start_time: float
    queue: Queue
    algorithm_execution_type: Algorithm

    def __init__(self, queue: Queue = None):
        super().__init__()
        self.queue = queue
        self.interrupt_event = threading.Event()

    def run(self):
        while len(self.queue.get_instance()) > 0:
            if self.interrupt_event.is_set():
                print(f"{self.__class__}{self.__class__.name}: CPU interrupt has been called")
                # stop cpu execution
                break
            print(
                f"{self.__class__}{self.__class__.name} processing queue: `{self.queue.get_instance()}` with scheduling algorithm: `{self.algorithm_execution_type.ALGORITHM_NAME}` as {self.algorithm_execution_type.EXECUTION_MODE.value}"
            )
            self.algorithm_execution_type.run(self.queue)
