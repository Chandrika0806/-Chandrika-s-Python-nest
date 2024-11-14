class Photograph:
    def __init__(self, name, size):
        self.name = name
        self.size = size  
        self.blocks = []  
    def __repr__(self):
        return f"{self.name} ({self.size} MB), Blocks: {self.blocks}"
class SequentialFileAllocation:
    def __init__(self, total_blocks=100, block_size=10):
        self.total_blocks = total_blocks
        self.block_size = block_size
        self.storage = [None] * total_blocks  # Initialize storage with None
        self.photographs = {}  # Dictionary to hold allocated photographs
    def allocate_photograph(self, photograph):
        required_blocks = (photograph.size + self.block_size - 1) // self.block_size  # Calculate required blocks
        # Find contiguous free blocks
        start_index = None
        for i in range(self.total_blocks):
            if self.storage[i] is None:  # Check for free block
                if start_index is None:
                    start_index = i
                if i - start_index + 1 == required_blocks:
                    break
            else:
                start_index = None  # Reset if a block is occupied
        if start_index is not None and start_index + required_blocks <= self.total_blocks:
            # Allocate blocks
            for i in range(start_index, start_index + required_blocks):
                self.storage[i] = photograph.name  # Store photograph name in storage
                photograph.blocks.append(i)  # Update photograph's block list
            self.photographs[photograph.name] = photograph  # Add to photographs dictionary
            print(f"Allocated: {photograph}")
        else:
            print(f"Failed to allocate {photograph.name}. Not enough contiguous space.")
    def delete_photograph(self, photograph_name):
        if photograph_name not in self.photographs:
            print(f"Photograph '{photograph_name}' not found.")
            return
        photograph = self.photographs[photograph_name]
        for block_index in photograph.blocks:
            self.storage[block_index] = None  # Mark the block as free
        del self.photographs[photograph_name]  # Remove from photographs dictionary
        print(f"Deleted photograph: {photograph_name}")
    def display_allocation_status(self):
        print("\nCurrent Storage Allocation:")
        for i in range(self.total_blocks):
            if self.storage[i] is None:
                print(f"Block {i}: Free")
            else:
                print(f"Block {i}: {self.storage[i]}")
    def calculate_total_disk_space_used(self):
        used_space = sum(1 for block in self.storage if block is not None) * self.block_size
        print(f"Total Disk Space Used: {used_space} MB out of {self.total_blocks * self.block_size} MB")
museum_collection = SequentialFileAllocation()
photo_a = Photograph("Portrait_1920s.jpg", 5)
photo_b = Photograph("Landscape_1930s.jpg", 15)
photo_c = Photograph("Architecture_1940s.jpg", 10)
photo_d = Photograph("Portrait_1950s.jpg", 20)
museum_collection.allocate_photograph(photo_a)
museum_collection.allocate_photograph(photo_b)
museum_collection.allocate_photograph(photo_c)
museum_collection.allocate_photograph(photo_d)
museum_collection.display_allocation_status()
museum_collection.calculate_total_disk_space_used()
museum_collection.delete_photograph("Portrait_1920s.jpg")
museum_collection.display_allocation_status()
museum_collection.calculate_total_disk_space_used()
