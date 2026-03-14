class Solution(object):
    def replaceElements(self, arr):
        max_right = -1
        for i in range(len(arr)-1, -1, -1):
            curr_val = arr[i]
            arr[i] = max_right
            if curr_val > max_right:
                max_right = curr_val
        return arr
        