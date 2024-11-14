class MediaFile:
    def __init__(self, name, file_type, size):
        self.name = name
        self.file_type = file_type
        self.size = size
        self.blocks = []
    def __repr__(self):
        return f"{self.name} ({self.file_type}), Size: {self.size} MB"
class DiskBlock:
    def __init__(self, index):
        self.index = index
        self.data = None
        self.next_block = None
class LinkedFileAllocation:
    def __init__(self, block_size=10):  
        self.disk = []  
        self.fat = {}  
        self.block_size = block_size
    def add_file(self, media_file):
        required_blocks = (media_file.size + self.block_size - 1) // self.block_size  # Calculate number of blocks needed
        block_indices = []
        for i in range(len(self.disk), len(self.disk) + required_blocks):
            self.disk.append(DiskBlock(i))  # Add new disk blocks
            block_indices.append(i)
        for i in range(required_blocks):
            if i < required_blocks - 1:
                self.disk[block_indices[i]].next_block = block_indices[i + 1]  # Link to the next block
            else:
                self.disk[block_indices[i]].next_block = None  # Last block points to None
        media_file.blocks = block_indices  # Store block indices in media file
        self.fat[media_file.name] = block_indices  # Update FAT
        print(f"Added: {media_file}")
    def delete_file(self, file_name):
        if file_name not in self.fat:
            print(f"File '{file_name}' not found.")
            return
        block_indices = self.fat[file_name]
        for block_index in block_indices:
            self.disk[block_index] = None  # Mark block as deleted
        del self.fat[file_name]
        print(f"Deleted file: {file_name}")
    def retrieve_file(self, file_name):
        if file_name not in self.fat:
            print(f"File '{file_name}' not found.")
            return None
        block_indices = self.fat[file_name]
        file_blocks = []
        for block_index in block_indices:
            if self.disk[block_index]:  # If block is not None
                file_blocks.append(self.disk[block_index])
        print(f"Retrieved file '{file_name}' with blocks: {file_blocks}")
        return file_blocks
    def display_files(self):
        print("Current Media Files:")
        for file_name, block_indices in self.fat.items():
            print(f"{file_name}: Blocks {block_indices}")
    def calculate_disk_space(self):
        total_space = len(self.disk) * self.block_size
        used_space = sum(self.block_size for block in self.disk if block is not None)
        print(f"Total Disk Space: {total_space} MB")
        print(f"Used Disk Space: {used_space} MB")
        print(f"Free Disk Space: {total_space - used_space} MB")
multimedia_app = LinkedFileAllocation()
file_a = MediaFile("Landscape.jpg", "Image", 5)
file_b = MediaFile("Concert.mp4", "Video", 50)
file_c = MediaFile("Song.mp3", "Audio", 8)
multimedia_app.add_file(file_a)
multimedia_app.add_file(file_b)
multimedia_app.add_file(file_c)
multimedia_app.display_files()
multimedia_app.retrieve_file("Concert.mp4")
multimedia_app.delete_file("Song.mp3")
multimedia_app.display_files()
multimedia_app.calculate_disk_space()
