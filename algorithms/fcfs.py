ALGORITHM_NAME = "First-Come-First-Serve"

test_processes = {
    'A': (0, 4),
    'B': (1, 9),
    'C': (4, 2),
    'D': (6, 7)
}


def fcfs_algorithm(
        arrival_service_pairs: dict,
        is_preemptive: bool
):
    for process_name, (process_arrival, process_service) in test_processes.items():
        exec(f"{process_name.lower()}_execution_time = {process_service}")
        exec(f"{process_name.lower()}_arrival_time = {process_arrival}")

        print(a_execution_time)

    average_turn_around_time = 0  # GOAL
    # wait time for each process # GOAL

    pass


if __name__ == "__main__":
    fcfs_algorithm(None, None)
