from collections import deque
def calculate_total_time(orders, time_quantum):
    order_queue = deque(orders)
    total_time = 0
    while order_queue:
        current_order = order_queue.popleft()
        if current_order <= time_quantum:
            total_time += current_order
        else:
            total_time += time_quantum
            order_queue.append(current_order - time_quantum)
    return total_time
orders = [5, 3, 8, 6]
time_quantum = 4
total_time = calculate_total_time(orders, time_quantum)
print(f"The total time required to complete all orders is: {total_time} minutes")
