
'''
processes have arrival times and service times.
steps:
1. calculate waiting time (wt).
2. calculate turnaround time = service time (st) + wt

1. calculate waiting time.

keep track of the process with the shortest rt.
when a process arrives:
    it gets added to queue
    once process is added to queue, you need to sort the processes by remaining time.
    if srt is lower than curr process rt:
        Add curr process to queue.
        queue.pop()
        queue.sort_by_rt()
        update srt



queue must be sorted after every insertion in descending order of their service times.
'''
import math
ALGORITHM_NAME = "ShortestTimeRemaining"



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

class Process:
    def __init__(self, process_name, arrival_time, service_time, remaining_time):
        self.process_name = process_name
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.remaining_time = remaining_time


# Function to increase the wait times of the processes every second they are in the waiting queue.
def increaseWaitTime(queue, wt):
    if queue:
        for process in queue:
            wt[process.process_name] = wt.get(process.process_name, 0) + 1


# Turnaround time = service time + wait time
def calculateTurnaroundTime(services, wt):
    tt = {}
    for key, val in services.items():
        tt[key] = val + wt.get(key, 0)
    return tt


def run(data):

    arrivals, services = convertData(data)
    n = len(services)
    # Waiting time
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

    queue = []
    currProcess = ""

    for i in range(max(sum(services.values()) + 1, latestLength)):
        print("time = ", i)

        # Increase the wait time for all the processes in queue
        increaseWaitTime(queue, wt)
        # If process arrives then begin servicing if no process currently running
        # If there is an existing process, add this to queue
        if i in arrivals:
            if currProcess != "":
                queue.append(currProcess)
                currProcess = ""
            for j in range(len(arrivals[i])):
                process_name = arrivals[i][j]
                arrival = i
                service = services[process_name]
                remaining = service
                process = Process(process_name, arrival, service, remaining)
                queue.append(process)
            # Sorting the queue in decreasing order of their service times
            queue.sort(key=lambda process: process.remaining_time, reverse=True)

            if currProcess == "" and queue:
                currProcess = queue.pop()

        # If no process has arrived, then currProcess is set to ""
        elif currProcess == "":
            continue

        # If the process had been completed, then remove from processor and pop process from queue
        if currProcess != "" and currProcess.remaining_time == 0:
            if queue:
                currProcess = queue.pop()
            else:
                currProcess = ""
        # If a process is running, reduce remaining time to completion by 1 second
        if currProcess != "" and currProcess.remaining_time != 0:
            currProcess.remaining_time -= 1

        if currProcess:
            print("Curr process:", currProcess.process_name)
            print(wt)

    print("wait times = ", dict(sorted(wt.items())))

    tt = calculateTurnaroundTime(services, wt)
    print("turnaround time =", tt)

    avg_tt = sum(tt.values()) / len(tt.values())
    print("Average turnaround time  =", avg_tt)

    return {
        "turnaroundtimes": tt,
        "averageTurnAroundTime": avg_tt
    }





if __name__ == "__main__":
    data = {
        'A': '(0, 10)',
        'B': '(3, 2)',
        'C': '(6, 8)',
        'D': '(8, 7)'
    }
    run(data)






