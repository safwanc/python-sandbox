'''
Longest Increasing Path (in a matrix)
'''

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

def brute_force(nums, i, j, min_threshold=float('-inf')):    
    if 0 <= i < len(nums) and 0 <= j < len(nums[0]) and nums[i][j] > min_threshold:
        min_threshold = nums[i][j]
        return 1 + max(brute_force(nums, i-1, j, min_threshold),
                       brute_force(nums, i+1, j, min_threshold),
                       brute_force(nums, i, j-1, min_threshold),
                       brute_force(nums, i, j+1, min_threshold))
    return 0

brute_force_wrapper = lambda nums: max(brute_force(nums, i, j) for i in range(len(nums)) for j in range(len(nums[0])))

def longest_increasing_path(nums):
    m, n = len(nums), len(nums[0])
    dp = [[0] * (n) for _ in range(m)]

    def dfs(i, j):
        if not dp[i][j]:
            val = nums[i][j]
            dp[i][j] = 1 + max(dfs(i-1, j) if 0 <= i-1 and nums[i-1][j] > val else 0,
                               dfs(i+1, j) if i+1 < m and nums[i+1][j] > val else 0,
                               dfs(i, j-1) if 0 <= j-1 and nums[i][j-1] > val else 0,
                               dfs(i, j+1) if j+1 < n and nums[i][j+1] > val else 0)
        return dp[i][j]
    
    return max(dfs(i,j) for i in range(m) for j in range(n))

print(brute_force_wrapper(nums))
print(longest_increasing_path(nums))