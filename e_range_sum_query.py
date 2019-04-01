class NumArray:

    def __init__(self, nums):
        self.dp = nums
        for i in xrange(1, len(nums)):
            self.dp[i] += self.dp[i-1]

    def sumRange(self, i, j):
        return self.dp[j] - (self.dp[i-1] if i>0 else 0) 

nums =[-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,5)
param_3 = obj.sumRange(0,5)

print(param_1)
print(param_2)
print(param_3)
