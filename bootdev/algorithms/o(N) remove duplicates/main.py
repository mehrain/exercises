def remove_duplicates(nums):
    filtered_nums = []
    for num in nums: 
        if num in filtered_nums:
            pass
        else: 
            filtered_nums.append(num)
    return filtered_nums
