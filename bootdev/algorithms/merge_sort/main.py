def merge_sort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left, right)


def merge(first, second):
    sorted_list = []
    i = j = 0
    for _ in range(len(first) + len(second)):
        if i < len(first) and (j >= len(second) or first[i] < second[j]):
            sorted_list.append(first[i])
            i += 1
        else:
            sorted_list.append(second[j])
            j += 1
    return sorted_list

