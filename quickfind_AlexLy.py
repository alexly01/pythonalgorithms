'''
name: Alexander Ly
studentID: 027744520

assignment:PA3
'''

import sys, re

class Solution:

	def partition(self, A: list[int], p: int, r: int)	-> int:
		# x is our pivot
		x = A[r]
        # i is our pointer
		i = p 

		for j in range(p, r):
			if (A[j] <= x):
				arr[i], arr[j] = arr[j], arr[i]
				i += 1
		arr[i], arr[r] = arr[r], arr[i]
		return i

	def kthSmallest(self, arr: list[int], left: int, right: int, k: int )	-> int:

		if (k > 0 and k <= right - left + 1):
			q = self.partition(arr, left, right)

		if (q - left == k - 1):
			return arr[q]
		if (q - left > k - 1):  
			return self.kthSmallest(arr, left, q - 1, k)
			
		return self.kthSmallest(arr, q + 1, right, k - q + left - 1)


if __name__ == '__main__':
	arr = [int(s) for s in re.findall("[-\d]+", sys.argv[1])]
	k = int(sys.argv[2])
	obj = Solution()
	print(arr, k)
	ret = obj.kthSmallest(arr, 0, len(arr) - 1, k)
	print(ret)