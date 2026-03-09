class Solution():
    def maxProfit(Self, nums):

        min_value = nums[0]
        max_difference = 0
        for i in range(1, len(nums)):

            diff = nums[i] - min_value

            if diff > max_difference:
                max_difference = diff

            if nums[i] < min_value:
                min_value = nums[i]
                
        return max_difference

obj=Solution()
print(obj.maxProfit([7,1,2,3,6,5]))
