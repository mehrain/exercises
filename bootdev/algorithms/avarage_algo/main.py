def average_followers(nums):
    sum = int(0)
    count = int(0)
    if len(nums) == 0:
        return None
    for num in nums:
        sum += num
        count += 1
    return sum / count