class MemoryBlock:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.allocated = False
        self.process_name = None

    def is_free(self):
        # Check if the memory block is free
        return not self.allocated

    def allocate(self, process_name):
        # Allocate the block to a process
        if self.is_free():
            self.allocated = True
            self.process_name = process_name
            return True
        return False

    def deallocate(self):
        # Deallocate the block, making it free
        self.allocated = False
        self.process_name = None

    def __str__(self):
        # Return a string representation of the memory block
        status = "Free" if not self.allocated else f"Allocated to {self.process_name}"
        return f"[Start: {self.start}, Size: {self.size}, Status: {status}]"

class MemoryManager:
    def __init__(self, total_memory):
        # Initialize memory manager with a single block of total memory size
        self.total_memory = total_memory
        self.memory_blocks = [MemoryBlock(0, total_memory)]

    def allocate_memory(self, process_name, size):
        # Find the first free block that can fit the requested size
        for block in self.memory_blocks:
            if block.is_free() and block.size >= size:
                # Split the block if it's larger than requested size
                if block.size > size:
                    new_block = MemoryBlock(block.start + size, block.size - size)
                    self.memory_blocks.append(new_block)
                    block.size = size
                block.allocate(process_name)
                return True
        print(f"Not enough memory to allocate for {process_name}.")
        return False

    def print_memory_status(self):
        # Print the current status of all memory blocks
        print("\nCurrent Memory Status:")
        for block in self.memory_blocks:
            print(block)

    def print_total_memory_used(self):
        # Calculate and print the total memory used
        total_used = sum(block.size for block in self.memory_blocks if block.allocated)
        print(f"\nTotal memory used: {total_used} units out of {self.total_memory} units.")

# Driver Code
memory_manager = MemoryManager(8000)

requests = [
    ("Emergency Department", 2000),
    ("Cardiology Department", 1500),
    ("Laboratory Information System", 1200),
    ("Radiology Department", 1800),
    ("Patient Management System", 1000),
    ("Pharmacy System", 600),
    ("Surgical Services", 2200)
]

for request in requests:
    process_name, size = request
    allocated = memory_manager.allocate_memory(process_name, size)
    if allocated:
        memory_manager.print_memory_status()

# Print total memory used after all allocations
memory_manager.print_total_memory_used()
