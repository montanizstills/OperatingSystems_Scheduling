import threading
import time

from queue import Queue


class QueueObserver(threading.Thread):

    def __init__(self):
        super().__init__()
        self.queue = Queue()
        self.previous_queue_count = 0
        self.interrupt_event = threading.Event()

    def get_queue_count(self):
        return len(self.queue.get_instance())

    def run(self):
        while True:
            if self.interrupt_event.is_set():
                print(f"Observer: `{self.__class__} interrupt has been set")  # TODO - remove 2
            print(f"Observer: `{self.__class__}` is running")  # TODO - remove 3
            time.sleep(1)  # TODO - remove 1
            if self.queue.arrival_flag:
                print(f"Observer: `{self.__class__}` has detected a new item added to the queue `{self.queue}`")
