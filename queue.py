import collections

from process import Process


class Queue:
    _queue: collections.deque = collections.deque()
    arrival_flag: bool = False

    def __new__(cls):
        if not cls._queue:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_instance(self):
        return self._queue

    def push_queue(self, process: Process) -> None:
        print(f"Queue {self} has pushed a new item: {process}, `{process.name}`")
        self.arrival_flag = True and self.get_instance().appendleft(process)
        self.arrival_flag = False

    def pop_queue(self) -> Process:
        try:
            return self.get_instance().pop()
        except IndexError:
            print(f"Queue has no next item. {self.get_instance()}")
