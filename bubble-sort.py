import time, timeit

def bubble_sort(arr):
    """
    Build the bad character table for Boyer-Moore algorithm.
    
    Args:
        arr: unsorted list 
    Returns:
        arr: sorted list
    """
    t1 = time.time()
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if not swapped:
            break
    t2 = time.time()
    print(f'Time taken : {t2 - t1} seconds')
    return arr

arr = [5, 1, 4, 2, 8]
# arr = [9,1,5,3,7,13,11]
# arr = [9,8,7,6,5,4]
result = bubble_sort(arr)
print(result)

# elapsed_time = timeit.timeit(stmt="bubble_sort(arr)", setup="from __main__ import bubble_sort; arr = [5, 1, 4, 2, 8]", number=100)
# print(f"Average time: {elapsed_time/100} seconds")