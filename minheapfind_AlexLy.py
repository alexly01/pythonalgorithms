'''
name: Alexander Ly	
studentID: 0027744520
assignment:PA3
'''

import sys, re

class Solution:

	def left(self, k: int )	-> int:
		return 2 * k + 1

	def right(self, k: int ) -> int:
		return 2 * k + 2

	def heapify(self, arr: list[int], k: int, heap_size: int)	-> int:
		l = self.left(k) 
		r = self.right(k)
		smallest  = k
		if ((l < heap_size and arr[l] < arr[k])):
			smallest = l
		else:
			smallest = k
		if ((r < heap_size and arr[r] < arr[smallest])):
			smallest = r
		if (smallest != k):
			arr[k], arr[smallest] = arr[smallest], arr[k]
			self.heapify(arr, smallest, heap_size)
	
	def buildHeap(self, arr: list[int])	-> int:
		heap_size = len(arr)
		for i in range (heap_size//2 - 1, -1, -1):
			self.heapify(arr, i, heap_size)

	def heapSort(self, arr: list[int])	-> int:
		heap_size = len(arr)
		self.buildHeap(arr)
		for i in range (heap_size - 1, -1, -1):
			arr[0], arr[i] = arr[i], arr[0]
			heap_size -= 1
			self.heapify(arr, 0, i)
			
	
	def pa3(self, arr: list[int], k: int)	-> int:
		retval = 0
		print(arr, k)
		self.heapSort(arr)
		retval = arr[k - 1]
		return retval 

if __name__ == '__main__':
	arr = [int(s) for s in re.findall("[-\d]+", sys.argv[1])]
	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)