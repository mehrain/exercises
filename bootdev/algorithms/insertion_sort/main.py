def insertion_sort(nums):
    for i in nums:
        j = nums.index(i)
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums
        
