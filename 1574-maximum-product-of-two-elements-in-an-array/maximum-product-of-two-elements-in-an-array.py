# class Solution(object):
#     def maxProduct(self, nums):
#         res = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 product = (nums[i] - 1) * (nums[j] - 1)
#                 if product >res:
#                     res = product
#         return res
# obj=Solution()
# print(obj.maxProduct([3,4,5,2]))        


class Solution():
    def maxProduct(self, nums):

        biggest_num = float('-inf')
        second_biggest = float('-inf')
        for i in nums:
            if i > biggest_num:
                second_biggest = biggest_num
                biggest_num = i
            elif i > second_biggest:
                second_biggest = i
        
        return (biggest_num-1) * (second_biggest-1)

obj=Solution()
print(obj.maxProduct([3,4,5,2]))
