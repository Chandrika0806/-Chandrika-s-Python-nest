class WorstFitMemoryManager:
    def __init__(self, memory_blocks):
        self.memory_blocks = memory_blocks
        self.available_blocks = {i: block for i, block in enumerate(memory_blocks)}
        self.processes = {}  # Store process_id and allocated block

    def allocate_memory(self, process_id, size):
        # Find the worst fit block (largest block that can fit the process)
        worst_fit_index = None
        worst_fit_size = -1

        for index, block in self.available_blocks.items():
            if block >= size and block > worst_fit_size:
                worst_fit_size = block
                worst_fit_index = index

        if worst_fit_index is not None:
            # Allocate memory
            self.processes[process_id] = worst_fit_index
            self.available_blocks[worst_fit_index] -= size  # Reduce block size by allocated size
            print(f"Allocated {size} units of memory for Process {process_id} in Block {worst_fit_index}.")
        else:
            print(f"Failed to allocate {size} units of memory for Process {process_id}: Not enough space.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            block_index = self.processes[process_id]
            size = self.memory_blocks[block_index] - self.available_blocks[block_index]
            self.available_blocks[block_index] += size  # Restore the original size of the block
            del self.processes[process_id]  # Remove the process from the list
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("\nMemory Status:")
        for index, block in self.available_blocks.items():
            total_size = self.memory_blocks[index]
            allocated_size = total_size - block
            print(f"Block {index}: {allocated_size}/{total_size} units allocated.")

# Driver Code
memory_manager = WorstFitMemoryManager([150, 300, 100, 200, 250, 50, 350, 180, 120, 200]) 
memory_manager.allocate_memory(1, 180)  # Should allocate to Block 6 (350 units)
memory_manager.allocate_memory(2, 400)  # Should fail (no block large enough)
memory_manager.allocate_memory(3, 120)  # Should allocate to Block 4 (250 units)
memory_manager.display_memory_status()

memory_manager.deallocate_memory(2)  # Should print "Process 2 not found"
memory_manager.deallocate_memory(1)  # Should deallocate from Block 6
print("\nAfter deallocating Process 1:")
memory_manager.display_memory_status()
