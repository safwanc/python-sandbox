nums = sorted([1, 2, 2])

result = [[]]

for i in range(len(nums)):

    if i == 0 or nums[i] != nums[i-1]:
        l = len(result)

    for j in range(len(result) - l, len(result)):
        result.append(result[j] + [nums[i]])

print(result)