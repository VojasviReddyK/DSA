class Solution():
    def removeElement(self, nums, val):

        slow = 0

        for fast in range(len(nums)):

            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow


obj = Solution()
nums = [1,2,3,3,4]
k = obj.removeElement(nums, 3)

print(k)
print(nums[:k])