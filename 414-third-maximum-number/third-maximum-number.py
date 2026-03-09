class Solution():
    def thirdMax(self, nums):

        firstLargest = float('-inf')
        secondLargest = float('-inf')
        thirdLargest = float('-inf')

        for i in range(len(nums)):

            if nums[i] > firstLargest:
                thirdLargest = secondLargest
                secondLargest = firstLargest
                firstLargest = nums[i]

            elif nums[i] > secondLargest and nums[i] != firstLargest:
                thirdLargest = secondLargest
                secondLargest = nums[i]

            elif nums[i] > thirdLargest and nums[i] != firstLargest and nums[i] !=           secondLargest:
                thirdLargest = nums[i]

        if thirdLargest == float('-inf'):
            return firstLargest
        return thirdLargest

obj = Solution()
print(obj.thirdMax([2,7,5,9,6]))
        