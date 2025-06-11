import time

def insertion_sort(arr):
    """
    Args:
        arr: unsorted list 
    Returns:
        arr: sorted list
    """
    # arr = [5, 1, 4, 2, 8]
    n = len(arr)
    for i in range(1, n-1):
        key = arr[i]
        j = i-1
        sorted = True
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            sorted = False
        
        if sorted:
            break
        arr[j + 1] = key
    return arr