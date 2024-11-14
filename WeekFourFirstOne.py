class MemoryVariableTechnique:
    def __init__(self, partitions):
        self.partitions = partitions
        self.memory_map = {
            1: [False] * partitions[1],
            2: [False] * partitions[2],
            3: [False] * partitions[3]
        }
        self.processes = {}
    def allocate_memory(self, process_id, size):
        for partition_id, partition in self.memory_map.items():
            if len(partition) >= size and all(not partition[i] for i in range(size)):
                # Allocate memory
                for i in range(size):
                    partition[i] = True
                self.processes[process_id] = (partition_id, size)
                print(f"Allocated {size} units of memory for Process {process_id} in Partition {partition_id}.")
                return
        print(f"Failed to allocate {size} units of memory for Process {process_id}.")
    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            partition_id, size = self.processes[process_id]
            for i in range(size):
                self.memory_map[partition_id][i] = False
            del self.processes[process_id]
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        for partition_id, partition in self.memory_map.items():
            allocated_units = sum(partition)
            total_units = len(partition)
            print(f"Partition {partition_id}: {allocated_units}/{total_units} units allocated.")
mvt = MemoryVariableTechnique({1: 300, 2: 500, 3: 200}) 
mvt.allocate_memory(1, 150) 
mvt.allocate_memory(2, 400) 
mvt.allocate_memory(3, 100) 
mvt.display_memory_status()
mvt.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
mvt.display_memory_status()
