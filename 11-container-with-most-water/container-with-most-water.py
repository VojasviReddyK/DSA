class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_v = 0
        
        while left < right:
            width = right - left
            curr_height = min(height[left],height[right])
            curr_area = width * curr_height

            if curr_area > max_v:
                max_v = curr_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_v
obj=Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
        