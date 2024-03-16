def find_max(nums):
    if nums == [] or nums == None:
        return 0 
    count = float('-inf')
    for num in nums: 
        if num > count:
            count = num
    return count