# BROTE FORCE METHOD O(n log n)
class Solution(object):
    def sortedSquares(self, nums):

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        nums.sort()
        return nums
obj=Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))

# TWO POINTERS METHOD
class Solution():
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -=1 
            pos -= 1

        return result
obj=Solution()
print(obj.sortedSquares([-4,0,-1,3,10]))

        