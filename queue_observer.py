import threading

from queue import Queue


class QueueObserver(threading.Thread):
    arriving_processes: dict
    queue: Queue
    previous_queue_count: int
    interrupt_event = threading.Event()

    def __init__(self):
        super().__init__()
        self.queue = Queue()
        self.previous_queue_count = 0

    def get_queue_count(self):
        return len(self.queue.get_instance())

    def run(self):
        while True:
            if self.queue.arrival_flag:
                print(f"{self.__class__} has detected the queue has been appended to.")
                # self.interrupt_event.set()


