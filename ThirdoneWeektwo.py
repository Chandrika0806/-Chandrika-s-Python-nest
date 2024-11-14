from queue import Queue
def calculate_total_time(high_priority_jobs, low_priority_jobs):
    job_queue = Queue()
    for job, time in high_priority_jobs.items():
        job_queue.put((job, time))
    for job, time in low_priority_jobs.items():
        job_queue.put((job, time))
    total_time = 0
    while not job_queue.empty():
        job, time = job_queue.get()
        total_time += time
    return total_time
high_priority_jobs = {'Job A': 15, 'Job B': 10, 'Job C': 20}
low_priority_jobs = {'Job D': 5, 'Job E': 8, 'Job F': 3}

total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all print jobs is: {total_time} units")
