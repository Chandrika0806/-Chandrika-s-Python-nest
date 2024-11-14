def calculate_total_time(arrival_times, pages):
    current_time = 0
    total_time = 0
    for i in range(len(arrival_times)):
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        current_time += pages[i] 
    return current_time
arrival_times = [0, 1, 3, 5]
pages = [10, 5, 3, 7] 
total_time = calculate_total_time(arrival_times, pages)
print(f"The total time taken to complete all printing tasks is: {total_time} seconds")
