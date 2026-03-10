# HASHMAP METHOD
class Solution(object):
    def checkIfExist(self, nums):
        seen = set()
        for i in nums:
            if (2 * i in seen) or (i % 2 == 0 and i // 2 in seen):
                return True
            seen.add(i)
        return False

obj=Solution()
print(obj.checkIfExist([10,2,5,3]))

# # BRUTE FORCE METHOD
# class Solution(object):
#     def checkIfExist(self, arr):
#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if i != j and arr[i] == 2 * arr[j]:
#                     return True
#         return False
# obj=Solution()
# print(obj.checkIfExist([10,2,5,3]))


        