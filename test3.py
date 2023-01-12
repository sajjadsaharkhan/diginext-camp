def min_swap_count(arr):
    n = len(arr)

    positions_array = [*enumerate(arr)]

    positions_array.sort(key=lambda it: it[1])
 
    visited_array = {k: False for k in range(n)}
 
    swap_count = 0
    for i in range(n):
 
        if visited_array[i] or positions_array[i][0] == i:
            continue
 
        cycle_size = 0
        j = i
 
        while not visited_array[j]:
            visited_array[j] = True
            j = positions_array[j][0]
            cycle_size += 1
 
        if cycle_size > 0:
            swap_count += (cycle_size - 1)
 
    return swap_count


print(min_swap_count([1,2,3,4,5,6,7])) # should print 0
