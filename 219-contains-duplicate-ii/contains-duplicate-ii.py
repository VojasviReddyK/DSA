class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}

        for i in range(len(nums)):
            if nums[i] in last_seen and i - last_seen[nums[i]] <= k:
                return True
            
            last_seen[nums[i]] = i
        
        return False

obj=Solution()
print(obj.containsNearbyDuplicate([1,2,3,1], 3))
        