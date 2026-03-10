class Solution(object):
    def sortedSquares(self, nums):

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        nums.sort()
        return nums
obj=Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
        