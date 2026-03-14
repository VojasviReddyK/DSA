class Solution(object):
    def missingNumber(self, nums):
        
        n = len(nums)
        expected_sum = n * (n+1) / 2
        actual_sum = sum(nums)

        return expected_sum - actual_sum

obj=Solution()
print(obj.missingNumber([3,0,1]))

        