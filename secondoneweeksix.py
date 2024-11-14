class Page: 
    def __init__(self, page_id, process_name=None): 
        self.page_id = page_id
        self.process_name = process_name  # None if the page is free

    def allocate(self, process_name): 
        self.process_name = process_name

    def deallocate(self): 
        self.process_name = None

    def __str__(self): 
        if self.process_name:
            return f"Page {self.page_id} | {self.process_name}"
        else:
            return f"Page {self.page_id} | Free"

class MemoryManager: 
    def __init__(self, num_pages, page_size): 
        self.num_pages = num_pages 
        self.page_size = page_size 
        self.pages = [Page(page_id) for page_id in range(num_pages)]

    def allocate_memory(self, process_name, num_pages_requested): 
        # Find all free pages
        free_pages = [page for page in self.pages if page.process_name is None]
        
        # Check if enough pages are available
        if len(free_pages) >= num_pages_requested:
            for i in range(num_pages_requested):
                free_pages[i].allocate(process_name)
            return True
        return False
     
    def print_memory_status(self): 
        for page in self.pages:
            print(page)
        print()  # Blank line for readability

    def print_total_memory_used(self): 
        used_pages = sum(1 for page in self.pages if page.process_name is not None)
        total_memory_used = used_pages * self.page_size
        print(f"Total memory used: {total_memory_used} units out of {self.num_pages * self.page_size} units\n")

# Driver Code 
memory_manager = MemoryManager(num_pages=200, page_size=8)

requests = [ 
        ("Student Records System", 40), 
        ("Faculty Management System", 25), 
        ("Library Information System", 30), 
        ("Online Learning Platform", 35), 
        ("Research Database", 50) 
]
     
for request in requests: 
    process_name, num_pages_requested = request 
    allocated = memory_manager.allocate_memory(process_name, num_pages_requested)
    if allocated: 
       print(f"Allocated {num_pages_requested} pages for {process_name}") 
       memory_manager.print_memory_status()
    else: 
       print(f"Not enough memory available for {process_name} (requested {num_pages_requested} pages)\n")

memory_manager.print_total_memory_used()
