'''
Name: Alexander Ly 
ID: 027744520
Class: CECS 328 Sec 04
Due Date: October 7, 2022
assignment:PA2
'''

import sys
import random
import time

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

	def pa2_insertionsort (self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)
		
		n = len(query_list)
		A = query_list

		# get the start time
		st = time.process_time()
		for i in range(0, n):
                        key = A[i]
                        j = i - 1
                        while (j >= 0) and (A[j] < key):
                                A[j+1] = A[j]
                                j = j-1
                        A[j+1] = key

    	# end of insertion sort
		
		et = time.process_time()
		res = et - st

		return [query_list, res]




if __name__ == '__main__':
	input_type = sys.argv[1]
	elements_count = int(sys.argv[2])
	seed = sys.argv[3]
	
	obj = Solution()
	ret = obj.pa2_insertionsort(input_type, elements_count, seed)
	print(ret)

