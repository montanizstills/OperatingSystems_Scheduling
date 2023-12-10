import time

from process import Process

ALGORITHM_NAME = "First-Come-First-Serve"

A = Process('A', 0, 4)
B = Process('B', 1, 9)
C = Process('C', 4, 2)
D = Process('D', 6, 7)
E = Process('E', 4, 7)
F = Process('F', 3, 12)


def get_next_earliest_process(processes: list) -> Process:
    early: Process = min(processes, key=lambda process: process.arrival_time)
    print(f"next earliest process: {early.name}")
    return early


def get_next_shortest_process(processes: list):
    shortest: Process = min(processes, key=lambda process: process.service_time)
    print(f"next earliest process: {shortest.name}")
    return shortest


def execute_process(process: Process):
    for _i in range(1, process.service_time + 1):
        print(f"executing process {process.name}...")
        print(f"Elapsed time {_i}")


def non_preemptive(processes: list):
    all_process_completion_time = 0
    while processes:
        cpu_start = time.time()
        process_to_execute = get_next_earliest_process(processes)
        execute_process(process_to_execute)
        processes.remove(process_to_execute)
        cpu_end = time.time()

    average_turn_around_time = 0  # GOAL
    # wait time for each process # GOAL


def preemptive(processes: list):
    pass


def fcfs_algorithm(
        processes: list,
        is_preemptive: bool
):
    if is_preemptive:
        preemptive(processes)
    non_preemptive(processes)


if __name__ == "__main__":
    fcfs_algorithm([A, B, C, D, E, F], False)
