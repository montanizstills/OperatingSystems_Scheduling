import collections

from algorithms.Algorithm import Algorithm


class CPU:
    executing_time: float

    def __init__(self):
        pass

    @staticmethod
    def run(queue: collections.deque, algorithm_type: Algorithm):
        print(f"CPU processing queue: `{queue.__str__()}`")
        # process_clock_start = time.time()
        while queue:
            algorithm_type.run(queue)
            exit(1)
