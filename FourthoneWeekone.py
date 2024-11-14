from queue import PriorityQueue
def calculate_total_time(patients):
    pq = PriorityQueue()
    for priority, treatment_time in patients:
        pq.put((priority, treatment_time))
    total_time = 0
    while not pq.empty(): 
        _, treatment_time = pq.get()
        total_time += treatment_time 
    return total_time
patients = [
    (1, 10),  # Patient A: Priority 1, Treatment time 10 minutes
    (2, 8),   # Patient B: Priority 2, Treatment time 8 minutes
    (3, 15),  # Patient C: Priority 3, Treatment time 15 minutes
    (4, 5)    # Patient D: Priority 4, Treatment time 5 minutes
]
total_time = calculate_total_time(patients)
print(f"The total time required to treat all patients is: {total_time} minutes")
