import threading
import time

from algorithm import Algorithm
from queue import Queue
from queue_observer import QueueObserver


class CPU(threading.Thread):
    algorithm_execution_type: Algorithm
    observer = QueueObserver()

    def __init__(self):
        super().__init__()
        self.queue = Queue()
        self.interrupt_event = threading.Event()
        self.executing_time: float
        self.total_elapsed_time: float
        self.process_execution_start_time: float
        self.observer.start()

    def run(self):
        while True:
            # if cpu thread stopped, stop observer thread
            if self.interrupt_event.is_set():
                self.observer.interrupt_event.set()
            # if cpu thread restarted, unblock observer thread
            if not self.interrupt_event.is_set():
                self.observer.interrupt_event.clear()
            # if queue empty, sleep cpu
            if len(self.queue.get_instance()) == 0:
                print(f"No work for {self.__class__}, going to sleep...")  # TODO - remove 2
                pass
                time.sleep(1)  # TODO - remove 1
            # if self.interrupt_event.is_set():
            #     print(f"`{self.__class__},{self.__class__.name}` interrupt has been set")
            #     # stop cpu execution
            #     break
            print(
                f"{self.__class__}{self.__class__.name} processing queue: `{self.queue.get_instance()}` with scheduling algorithm: `{self.algorithm_execution_type.ALGORITHM_NAME}` as {self.algorithm_execution_type.EXECUTION_MODE.value}"
            )
            self.algorithm_execution_type.run(self.queue)
            # self.interrupt_event.set() # if set must be removed manually
