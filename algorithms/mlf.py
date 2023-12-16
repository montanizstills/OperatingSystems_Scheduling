ALGORITHM_NAME = "Multilevel-Feedback"

import math
from collections import deque
ALGORITHM_NAME = "Multi-Level Feedback"


def convertData(data):
    processes = []

    for key in data:
        item = eval(data[key])
        arrival = item[0]
        service = item[1]
        # print(arrival)
        # exit(1)
        processes.append(Process(key, arrival, service))

    return processes


def calculateQuantum(processes):
    quantum = 0
    avg_st = (sum([process.service_time for process in processes]) / len(processes))
    if math.ceil(avg_st) == avg_st:
        quantum = avg_st + 1
    else:
        quantum = math.ceil(avg_st)
    return int(quantum)


class Process:
    def __init__(self, name, arrival_time, service_time):
        self.name = name
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.remaining_service_time = service_time
        self.priority = 0  # Priority level (lower values mean higher priority)

    def execute(self, time_quantum):
        if self.remaining_service_time <= time_quantum:
            time_executed = self.remaining_service_time
            self.remaining_service_time = 0

        else:
            time_executed = time_quantum
            self.remaining_service_time -= time_quantum
        return time_executed


def multilevel_feedback_queue(processes, time_quantum):
    queues = [[] for _ in range(3)]  # Three priority queues

    current_time = 0
    completed_processes = []

    while processes or any(queue for queue in queues):
        # Move processes to the appropriate queue based on arrival time
        while processes and processes[0].arrival_time <= current_time:
            queues[0].append(processes.pop(0))

        for i in range(2):  # Start from the highest priority queue
            if queues[i]:
                current_process = queues[i][0]
                time_executed = current_process.execute(time_quantum)
                current_time += time_executed

                if current_process.remaining_service_time == 0:
                    completed_processes.append((current_process.name, current_time))
                    queues[i].pop(0)
                elif i < 2:  # Move to a lower priority queue if not in the lowest already
                    current_process.priority += 1
                    queues[i + 1].append(queues[i].pop(0))
                break

    return completed_processes


# Example usage
if __name__ == "__main__":
    data = {
        'A': '(0, 3)',
        'B': '(2, 6)',
        'C': '(4, 4)',
        'D': '(6, 5)',
        'E': '(8, 2)'
    }
    processes = convertData(data)
    # time_quantum = calculateQuantum(processes)
    time_quantum = 4
    print(time_quantum)
    result = multilevel_feedback_queue(processes, time_quantum)

    print("Process Execution Order:")
    for process, completion_time in result:
        print(f"{process} completed at time {completion_time}")
