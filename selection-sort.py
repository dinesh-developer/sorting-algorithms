import time

def selection_sort(arr):
    """
    Args:
        arr: unsorted list 
    Returns:
        arr: sorted list
    """
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr = [9,8,7,6,5,4]
result = selection_sort(arr)
print(result)