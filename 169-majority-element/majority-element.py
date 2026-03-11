class Solution(object):
    def majorityElement(self, nums):
        count = {}
        max_val = len(nums) // 2
        
        for i in nums:
            count[i] = count.get(i, 0) + 1
            
            if count[i] > max_val:
                return i
        
obj=Solution()
print(obj.majorityElement([2,1,2,2,2,3,1]))
            
        