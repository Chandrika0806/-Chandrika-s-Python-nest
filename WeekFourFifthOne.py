class PagingMemoryManager:
    def __init__(self, num_pages, page_size):
        self.num_pages = num_pages
        self.page_size = page_size
        self.available_pages = [True] * num_pages  # True means the page is free
        self.processes = {}  # Store process_id and list of allocated pages

    def allocate_memory(self, process_id, size):
        required_pages = (size + self.page_size - 1) // self.page_size  # Calculate pages needed
        allocated_pages = []

        for i in range(self.num_pages):
            if self.available_pages[i]:  # Check if the page is free
                allocated_pages.append(i)  # Add page index to allocated list
                self.available_pages[i] = False  # Mark the page as occupied
                if len(allocated_pages) == required_pages:  # If all required pages are allocated
                    break

        if len(allocated_pages) == required_pages:
            self.processes[process_id] = allocated_pages  # Store allocated pages for the process
            print(f"Allocated {size} bytes (in {required_pages} pages) for Process {process_id}: Pages {allocated_pages}.")
        else:
            print(f"Failed to allocate {size} bytes for Process {process_id}: Not enough free pages.")

    def deallocate_memory(self, process_id):
        if process_id in self.processes:
            allocated_pages = self.processes[process_id]
            for page in allocated_pages:
                self.available_pages[page] = True  # Mark each page as free
            del self.processes[process_id]  # Remove the process from the dictionary
            print(f"Deallocated memory for Process {process_id}.")
        else:
            print(f"Process {process_id} not found.")

    def display_memory_status(self):
        print("\nMemory Status:")
        for i in range(self.num_pages):
            status = "Allocated" if not self.available_pages[i] else "Free"
            print(f"Page {i}: {status}")

# Driver Code
memory_manager = PagingMemoryManager(num_pages=20, page_size=200) 
memory_manager.allocate_memory(1, 400)  # Should allocate 2 pages
memory_manager.allocate_memory(2, 600)  # Should allocate 3 pages
memory_manager.allocate_memory(3, 300)  # Should allocate 2 pages
memory_manager.display_memory_status()
memory_manager.deallocate_memory(2)  # Deallocate memory for Process 2
print("\nAfter deallocating Process 2:")
memory_manager.display_memory_status()
