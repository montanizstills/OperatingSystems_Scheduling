ALGORITHM_NAME = "First-Come-First-Serve"

time_quantum  = 5
test_processes = {
    'A': (0, 4,4),
    'B': (1, 9,9),
    'C': (4, 2,9),
    'D': (6, 7,9)
}


def fcfs_algorithm(
        arrival_service_pairs: dict,
        is_preemptive: bool
):
    cpu_start = 0
    cpu_end = 0;

    for process_name, (process_arrival, process_service) in test_processes.items():
        process_time_remaining = test_processes[process_name][2]


    average_turn_around_time = 0  # GOAL
    # wait time for each process # GOAL

    pass


if __name__ == "__main__":
    fcfs_algorithm(None, None)
