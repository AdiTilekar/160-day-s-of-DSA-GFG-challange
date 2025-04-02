class Solution:
    def getSecondLargest(self, arr):
        arr=list(set(arr))
        if len(arr) < 2:
            return -1
        arr.sort(reverse=True)
        return arr[1]
