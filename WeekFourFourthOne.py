class MFTMemoryManager:
    def __init__(self, num_partitions, partition_size):
        self.num_partitions = num_partitions
        self.partition_size = partition_size
        self.available_partitions = [True] * num_partitions  # True means partition is free
        self.processes = {}  # Store process_id and allocated partition

    def allocate_memory(self, process_id, size):
        if size > self.partition_size:
            print(f"Failed to allocate {size} units of memory for Process {process_id}: Size exceeds partition size.")
            return

        # Find a free partition to allocate
        for i in range(self.num_partitions):
            if self.available_partitions[i]:  # Check if partition is free
                self.available_partitions[i] = False  # Mark partition as occupied
                self.processes[process_id] = i  # Store process id and partition index
                print(f"Allocated {size} units of memory for Process {process_id} in Partition {i}.")
                return

        print(f"Failed to allocate {size} units of memory for Process {process_id}: No free partition available.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_index = self.processes[process_id]
            self.available_partitions[partition_index] = True  # Mark partition as free
            del self.processes[process_id]  # Remove the process from the dictionary
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("\nMemory Status:")
        for i in range(self.num_partitions):
            status = "Allocated" if not self.available_partitions[i] else "Free"
            print(f"Partition {i}: {status}")

# Driver Code
memory_manager = MFTMemoryManager(num_partitions=8, partition_size=800) 
memory_manager.allocate_memory(1, 600) 
memory_manager.allocate_memory(2, 900)  # Should fail because it's larger than the partition size
memory_manager.allocate_memory(3, 400)  # Should also fail since no partitions are free
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2)  # Should not find Process 2 to deallocate
memory_manager.deallocate_memory(1) 
print("\nAfter deallocating Process 1:")
memory_manager.display_memory_status()
