# BRUTE FORCE METHOD

# class Solution:
#     def twoSum(self, nums, target):

#         for i in range(len(nums)):
#             for j in range (i+1, len(nums)):
#                 if nums[i] + nums[j] ==  target:
#                     return [i, j]

# obj=Solution()
# print(obj.twoSum([2,7,5,15], 17))

# HASHMAP METHOD

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return (hashmap[complement], i)

            hashmap[nums[i]] = i

obj = Solution()
print(obj.twoSum([2,7,5,15], 17))