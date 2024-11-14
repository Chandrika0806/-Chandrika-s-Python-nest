from queue import Queue
def calculate_total_time(system_processes, user_processes):
    process_queue = Queue()
    for process, time in system_processes.items():
        process_queue.put((process, time))
    for process, time in user_processes.items():
        process_queue.put((process, time))
    total_time = 0
    while not process_queue.empty():
        process, time = process_queue.get()
        total_time += time
    return total_time
system_processes = {'Process A': 5, 'Process B': 3, 'Process C': 7}
user_processes = {'Process D': 4, 'Process E': 2, 'Process F': 6}
total_time = calculate_total_time(system_processes, user_processes)
print(f"The total time required to complete all processes is: {total_time} units")
