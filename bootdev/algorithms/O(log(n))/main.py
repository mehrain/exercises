def binary_search(target, arr):
    low = 0 
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] < target:
            low = median + 1 
        else: 
            high = median -1 
    if low != len(arr) and arr[low] == target:
        return True
    else: 
        return False
