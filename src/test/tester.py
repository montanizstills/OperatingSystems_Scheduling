import time

from src.main.algorithm import *
from src.main.cpu import CPU

if __name__ == '__main__':
    # given
    # A = Process('A', 0, 5)
    # B = Process('B', 1, 2)
    # C = Process('C', 4, 6)
    # D = Process('D', 6, 3)
    # E = Process('E', 4, 8)
    # F = Process('F', 3, 9)
    A = Process('A', 0, 1)
    B = Process('B', 1, 1)
    C = Process('C', 4, 1)
    D = Process('D', 6, 1)
    E = Process('E', 4, 1)
    F = Process('F', 3, 1)


    cpu = CPU()
    algorithm_type = FirstComeFirstServe(Algorithm.ExecutionMode.NON_PREEMPTIVE)
    cpu.algorithm_execution_type = algorithm_type

    # when
    cpu.start()
    cpu.queue.push_queue(A)
    cpu.queue.push_queue(C)
    cpu.queue.push_queue(B)

    cpu.queue.push_queue(D)
    cpu.queue.push_queue(F)
    cpu.queue.push_queue(E)
    time.sleep(1)
    cpu.queue.push_queue(C)
    cpu.queue.push_queue(A)
    cpu.queue.push_queue(F)
    time.sleep(20)
    cpu.queue.push_queue(B)
    # then
    # test cases
