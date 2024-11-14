def worst_fit_allocation(memory_blocks, program_requests):
    allocations = {}
    for program, request_size in program_requests.items():
        worst_fit_index = -1
        max_block_size = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= request_size and memory_blocks[i] > max_block_size:
                max_block_size = memory_blocks[i]
                worst_fit_index = i
        if worst_fit_index != -1:
            allocations[program] = request_size
            memory_blocks[worst_fit_index] -= request_size  
        else:
            allocations[program] = None  
    return allocations, memory_blocks
memory_blocks = [400, 250, 350, 200, 150]
program_requests = {'Program A': 150, 'Program B': 300, 'Program C': 200}
allocations, remaining_memory = worst_fit_allocation(memory_blocks, program_requests)
for program, allocated_memory in allocations.items():
    if allocated_memory is not None:
        print(f"{program} allocated {allocated_memory} units of memory.")
    else:
        print(f"{program} could not be allocated any memory.")
print("\nRemaining Memory in Memory Blocks:")
for i in range(len(memory_blocks)):
    print(f"Block {i+1}: {memory_blocks[i]} units")
