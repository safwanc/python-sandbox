'''
Longest Increasing Subsequence
'''

nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]

def brute_force(nums, i=len(nums), upper_bound=float('inf')):
    if i == 0: return 0
    elif nums[i-1] > upper_bound: return brute_force(nums, i-1, upper_bound)
    else: return max(1 + brute_force(nums, i-1, nums[i-1]), brute_force(nums, i-1, upper_bound))

def lis(nums):
    dp = [1] * len(nums)

    for i in range(len(dp)):
        for j in range(0, i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1        
    return max(dp)

print(brute_force(nums))
print(lis(nums))
