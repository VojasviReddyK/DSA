class Solution(object):
    def searchInsert(self, nums, target):

        for i in range(len(nums)):

            if nums[i] == target:
                return i

            if nums[i] > target:
                return i

        return len(nums)


obj = Solution()
print(obj.searchInsert([1,3,5,6], 9))
        