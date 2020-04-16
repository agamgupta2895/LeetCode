nums = [1,2,3,4]
result = []
res, n = [], len(nums)
for i in range(1, n, 2):
    temp = [nums[i]] * nums[i-1]
    res.extend(temp)