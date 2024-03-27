def quick_sort(nums, low, high):
    if low < high:
        partition_index = partition(nums, low, high)
        quick_sort(nums, low, partition_index - 1)
        quick_sort(nums, partition_index + 1, high)


def partition(nums, low, high):
    pivot = nums[high]
    i = low
    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i
