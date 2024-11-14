from queue import Queue
def calculate_total_time(high_priority_jobs, medium_priority_jobs, low_priority_jobs):
    job_queue = Queue()
    for job, time in high_priority_jobs.items():
        job_queue.put((job, time))
    for job, time in medium_priority_jobs.items():
        job_queue.put((job, time))
    for job, time in low_priority_jobs.items():
        job_queue.put((job, time))
    total_time = 0
    while not job_queue.empty():
        _, time = job_queue.get()
        total_time += time
    return total_time
high_priority_jobs = {'Job A': 20, 'Job B': 15, 'Job C': 25}
medium_priority_jobs = {'Job D': 10, 'Job E': 12, 'Job F': 8}
low_priority_jobs = {'Job G': 5, 'Job H': 4, 'Job I': 6}
total_time = calculate_total_time(high_priority_jobs, medium_priority_jobs, low_priority_jobs)
print(f"The total time required to complete all jobs is: {total_time} units")
