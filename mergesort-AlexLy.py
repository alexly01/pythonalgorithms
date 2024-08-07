'''
name1: AJ1 Fahim1
name2: AJ2 Fahim2

assignment:PA2
'''
import sys
import random
import time
import math

class Solution:
	
	#This function returns a descending sorted array.
	def function_a (self, elements_count: int) -> list:
		output = []
		for i in range(elements_count,0, -1):
			output.append(i)
		return output

	#This function returns an ascending sorted array.	
	def function_b (self, elements_count: int) -> list:
		output = []
		for i in range(1, elements_count):
			output.append(i)
		return output

	def function_c(self, elements_count: int, seed: int):
		output = []
		random.seed(seed)
		for i in range(0,elements_count+1):
			output.append(random.randint(1,1000000))

		return output


	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if 	input_type == "b":
			output = self.function_b(elements_count)
		if 	input_type == "c":
			output = self.function_c(elements_count, seed)
		return output
	
	
	def merge (self, A, left, middle, right):
		leftA = A[left:middle]
		rightA = A[middle:right]
		k = left
		i = j = 0

		while (left + i < middle and middle + j < right):
			if (leftA[i] >= rightA[j]):
				A[k] = leftA[i]
				i = i + 1
			else: 
				A[k] = rightA[j]
				j = j + 1
			k = k + 1
		if left + i < middle:
			while k < right:
				A[k] = leftA[i]
				i = i + 1
				k = k + 1
		else:
			while k < right:
				A[k] = rightA[j]
				j = j + 1
				k = k + 1
	
	
	def mergesort (self, A, left, right):
		if right - left > 1:
			middle = (left + right) // 2
			self.mergesort (A, left, middle)
			self.mergesort (A, middle, right)
			self.merge (A, left, middle, right)


	def pa2_mergesort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)

		# get the start time
		st = time.process_time()
		sys.setrecursionlimit(1500)
		self.mergesort(query_list, 0, n-1)
    	# your merge sort algorithm comes here ...

    	# end of merge sort
		
		et = time.process_time()
		res = et - st

		return [query_list, res]




if __name__ == '__main__':
	input_type = sys.argv[1]
	elements_count = int(sys.argv[2])
	seed = sys.argv[3]
	
	obj = Solution()
	ret = obj.pa2_mergesort(input_type, elements_count, seed)
	print(ret)

