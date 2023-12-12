import collections
import threading

from cpu import CPU


class QueueObserver(threading.Thread):
    queue: collections.deque
    previous_queue_count: int
    cpu: CPU

    def __init__(self, queue):
        super().__init__()

    def get_queue_count(self):
        return len(self.queue)

    def run(self):
        while self.is_alive():
            if self.get_queue_count() < self.previous_queue_count:
                self.cpu.interrupt_event.set()
                self.previous_queue_count += 1
