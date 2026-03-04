class Solution():
    def maxProfit(self, nums):

        min_val = nums[0]
        max_difference = 0
        for i in range(1, len(nums)):

                diff = nums[i] - min_val
                
                if diff > max_difference:
                    max_difference = diff

                if nums[i] < min_val:
                    min_val = nums[i]

        return max_difference


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
        