from queue import Queue
def calculate_total_time(high_priority_tasks, low_priority_tasks):
    task_queue = Queue()
    for task, time in high_priority_tasks.items():
        task_queue.put((task, time))
    for task, time in low_priority_tasks.items():
        task_queue.put((task, time))
    total_time = 0
    while not task_queue.empty():
        _, time = task_queue.get()
        total_time += time
    return total_time
high_priority_tasks = {'Task A': 12, 'Task B': 8, 'Task C': 15}
low_priority_tasks = {'Task D': 6, 'Task E': 4, 'Task F': 10}
total_time = calculate_total_time(high_priority_tasks, low_priority_tasks)
print(f"The total time required to complete all tasks is: {total_time} units")
