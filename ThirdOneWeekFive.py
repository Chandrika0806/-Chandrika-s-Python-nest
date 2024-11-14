class MemoryBlock:
    def __init__(self, start, size):
        self.start = start
        self.size = size
        self.allocated = False
        self.process_name = None
    def is_free(self):
        return not self.allocated
    def allocate(self, process_name):
        if self.is_free():
            self.allocated = True
            self.process_name = process_name
            return True
        return False
    def deallocate(self):
        self.allocated = False
        self.process_name = None
    def __str__(self):
        status = "Free" if not self.allocated else f"Allocated to {self.process_name}"
        return f"[Start: {self.start}, Size: {self.size}, Status: {status}]"
class MemoryManager:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.memory_blocks = [MemoryBlock(0, total_memory)]
    def allocate_memory(self, process_name, size):
        for block in self.memory_blocks:
            if block.is_free() and block.size >= size:
                if block.size > size:
                    new_block = MemoryBlock(block.start + size, block.size - size)
                    self.memory_blocks.append(new_block)
                    block.size = size
                block.allocate(process_name)
                return True
        print(f"Not enough memory to allocate for {process_name}.")
        return False
    def print_memory_status(self):
        print("\nCurrent Memory Status:")
        for block in self.memory_blocks:
            print(block)
    def print_total_memory_used(self):
        total_used = sum(block.size for block in self.memory_blocks if block.allocated)
        print(f"\nTotal memory used: {total_used} units out of {self.total_memory} units.")
memory_manager = MemoryManager(5000)
requests = [
    ("TrafficControl", 1200),
    ("RoutePlanning", 800),
    ("VehicleMonitoring", 1500),
    ("PassengerInformation", 600),
    ("MaintenanceLogistics", 700)
]
for request in requests:
    process_name, size = request
    allocated = memory_manager.allocate_memory(process_name, size)
    if allocated:
        memory_manager.print_memory_status() 
memory_manager.print_total_memory_used()
