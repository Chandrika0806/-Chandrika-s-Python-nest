class File:
    def __init__(self, file_id, file_size):
        self.file_id = file_id
        self.file_size = file_size  # Size in KB
        self.blocks = []  # List to hold allocated block indices
    def __repr__(self):
        return f"File ID: {self.file_id}, Size: {self.file_size} KB, Blocks: {self.blocks}"
class IndexSequentialFileAllocation:
    def __init__(self, total_blocks=1000, block_size=8):
        self.total_blocks = total_blocks
        self.block_size = block_size
        self.storage = [None] * total_blocks  # Initialize storage with None
        self.index = {}  # Dictionary to map file IDs to their blocks
    def allocate_file(self, file):
        required_blocks = (file.file_size + self.block_size - 1) // self.block_size  # Calculate required blocks
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
            for i in range(start_index, start_index + required_blocks):
                self.storage[i] = file.file_id  # Store file ID in storage
                file.blocks.append(i)  # Update file's block list
            self.index[file.file_id] = file.blocks  # Update index
            print(f"Allocated: {file}")
        else:
            print(f"Failed to allocate {file.file_id}. Not enough contiguous space.")
    def delete_file(self, file_id):
        if file_id not in self.index:
            print(f"File ID '{file_id}' not found.")
            return
        blocks = self.index[file_id]
        for block_index in blocks:
            self.storage[block_index] = None  # Mark the block as free
        del self.index[file_id]  # Remove from index
        print(f"Deleted file: {file_id}")
    def retrieve_file(self, file_id):
        if file_id not in self.index:
            print(f"File ID '{file_id}' not found.")
            return None
        blocks = self.index[file_id]
        print(f"Retrieved file '{file_id}' with blocks: {blocks}")
        return blocks
    def display_allocation_status(self):
        print("\nCurrent Storage Allocation:")
        for i in range(self.total_blocks):
            if self.storage[i] is None:
                print(f"Block {i}: Free")
            else:
                print(f"Block {i}: {self.storage[i]}")
    def calculate_total_disk_space_used(self):
        used_space = sum(1 for block in self.storage if block is not None) * self.block_size
        print(f"Total Disk Space Used: {used_space} KB out of {self.total_blocks * self.block_size} KB")
os_enterprise_x = IndexSequentialFileAllocation()
file_a = File("DB_Records", 50)  # 50 KB
file_b = File("Video_Clip", 80)   # 80 KB
file_c = File("Image_File", 16)   # 16 KB
file_d = File("Large_Database", 120)  # 120 KB
os_enterprise_x.allocate_file(file_a)
os_enterprise_x.allocate_file(file_b)
os_enterprise_x.allocate_file(file_c)
os_enterprise_x.allocate_file(file_d)
os_enterprise_x.display_allocation_status()
os_enterprise_x.retrieve_file("DB_Records")
os_enterprise_x.delete_file("Image_File")
os_enterprise_x.display_allocation_status()
os_enterprise_x.calculate_total_disk_space_used()
