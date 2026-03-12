class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return None
        n = len(arr)
        i = 0
        j = len(arr) - 1
        while i + 1 < n and arr[i] < arr[i+1]:
            i += 1
        while j > 0 and arr[j] < arr[j-1]:
            j -= 1
        return i == j and i > 0 and i < n - 1