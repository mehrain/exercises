def find_minimum(nums):
    minimum = float("inf")
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
