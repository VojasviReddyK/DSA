class Solution():
    def removeDuplicates(self, nums):

        if not nums:
            return None

        slow = 0

        for fast in range(1, len(nums)):

            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1

obj = Solution()
nums = [1,2,3,3,4]
k = obj.removeDuplicates(nums)

print(k)
print(nums[:k])

