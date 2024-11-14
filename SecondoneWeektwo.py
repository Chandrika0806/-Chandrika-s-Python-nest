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
high_priority_jobs = {'Job A': 8, 'Job B': 5, 'Job C': 10}
low_priority_jobs = {'Job D': 6, 'Job E': 3, 'Job F': 7}

total_time = calculate_total_time(high_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
