# Day 2 :- Move all zeros to end
class Solution:
	def pushZerosToEnd(self,arr):
	    j =c 0
	    for i in range(len(arr)):
	        if arr[i]!=0:
	            arr[i],arr[j] = arr[j],arr[i]
	            j+=1
