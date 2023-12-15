'''
processes have arrival times and service times.
steps:
1. calculate waiting time (wt).
2. calculate turnaround time = service time (st) + wt

1. calculate waiting time.
when a process arrives:
    all other processes in queue increase their wt by one.
    the process waits for its turn
    1. a process finishes executing - dequeue next process
'''
import math
from collections import deque
ALGORITHM_NAME = "FCFS"


def convertData(data):
    arrivals = {}
    services = {}

    for key in data:
        item = eval(data[key])
        services[key] = item[1]
    for key in data:
        item = eval(data[key])
        arrival = item[0]
        # print(arrival)
        # exit(1)
        if arrival in arrivals:
            arrivals[arrival] = arrivals[arrival].append(key)
        else:
            arrivals[arrival] = [key]
    return arrivals, services

def run(data):
    arrivals, services = convertData(data)
    n = len(services)
    print("arrivals", arrivals)
    print("services", services)
    #waiting time
    wt = {}

    # Setting up latestLength to see how many seconds we have to loop to.
    latestArrival = max(arrivals.keys())
    longestService = 0
    for process in arrivals[latestArrival]:
        longestService = max(longestService, services[process])
    latestLength = latestArrival + longestService

    # Initializing remaining service time
    rt = {}

    # Initially remaining time is the same as service time
    for i in services.keys():
        rt[i] = services[i]

    queue = deque()
    currProcess = ""

    # Count to check whether process has executed up to quantum
    for i in range(max(sum(services.values()) + 1, latestLength)):
        # Increase the wait time for all the processes in queue
        increaseWaitTime(queue, wt)

        # If process arrives then begin servicing if no process currently running
        # If there is an existing process, add this to queue
        if i in arrivals:
            if currProcess == "":
                currProcess = arrivals[i][0]
                for j in range(1, len(arrivals[i])):
                    queue.append(arrivals[i][j])
            else:
                for j in range(len(arrivals[i])):
                    queue.append(arrivals[i][j])

        # If no process has arrived, then currProcess is set to ""
        elif currProcess == "":
            continue

        # If the process had been completed, then remove from processor and pop process from queue
        if currProcess != "" and rt[currProcess] == 0:
            if queue:
                currProcess = queue.popleft()
            else:
                currProcess = ""

        # If a process is running, reduce remaining time to completion by 1 second
        if currProcess != "":
            rt[currProcess] -= 1

    print("wait times = ", dict(sorted(wt.items())))

    tt = calculateTurnaroundTime(services, wt)
    print("turnaround time =", tt)

    avg_tt = sum(tt.values()) / len(tt.values())
    print("Average turnaround time  =", avg_tt)

    return {
        "turnaroundtimes": tt,
        "averageTurnAroundTime": avg_tt
    }




# Function to increase the wait times of the processes every second they are in the waiting queue.
def increaseWaitTime(queue, wt):
    if queue:
        for process in queue:
            wt[process] = wt.get(process, 0) + 1


# Turnaround time = service time + wait time
def calculateTurnaroundTime(services, wt):
    tt = {}
    for key, val in services.items():
        tt[key] = val + wt.get(key, 0)
    return tt


if __name__ == "__main__":
    data = {
        'A': '(0, 10)',
        'B': '(3, 2)',
        'C': '(6, 8)',
        'D': '(8, 7)'
    }
    run(data)








