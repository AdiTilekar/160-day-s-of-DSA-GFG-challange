def reverse(arr,start,stop):
    while start<stop:
        arr[start],arr[stop]=arr[stop],arr[start]
        start+=1
        stop-=1

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d %=n
        reverse(arr,0,d-1)
        reverse(arr,d,n-1)
        reverse(arr,0,n-1)
        
