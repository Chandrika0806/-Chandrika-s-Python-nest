class BestFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.available_blocks = {i: block for i, block in enumerate(memory_blocks)}
        self.processes = {}

    def allocate_memory(self, process_id, size):
        # Find the best fit block
        best_fit_index = None
        best_fit_size = float('inf')

        for index, block in self.available_blocks.items():
            if block >= size and (block < best_fit_size):
                best_fit_size = block
                best_fit_index = index

        if best_fit_index is not None:
            # Allocate memory
            self.processes[process_id] = size
            self.available_blocks[best_fit_index] -= size
            print(f"Allocated {size} units of memory for Process {process_id} in Block {best_fit_index}.")
        else:
            print(f"Failed to allocate {size} units of memory for Process {process_id}.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            size = self.processes[process_id]
            for index, block in self.available_blocks.items():
                # Find the block where the process was allocated
                if block < self.memory_blocks[index]:
                    self.available_blocks[index] += size
                    del self.processes[process_id]
                    print(f"Deallocated memory for Process {process_id}.")
                    return
            print(f"Process {process_id} not found.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("\nMemory Status:")
        for index, block in self.available_blocks.items():
            total_size = self.memory_blocks[index]
            allocated_size = total_size - block
            print(f"Block {index}: {allocated_size}/{total_size} units allocated.")

# Driver Code
memory_manager = BestFitMemoryManager([100, 200, 50, 150, 300, 80, 120, 200]) 
memory_manager.allocate_memory(1, 70) 
memory_manager.allocate_memory(2, 180) 
memory_manager.allocate_memory(3, 250)
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2) 
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
