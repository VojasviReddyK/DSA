class Solution(object):
    def singleNumber(self, nums):
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        for i in hashmap:
            if hashmap[i] == 1:
                return i
obj=Solution()
print(obj.singleNumber([2,2,1]))
        