
import numpy as np

# input number of an array with gap between them 
# e.g. 1 5 10 11 21 2 15  in the input 

str_arr = input().split(' ')

arr = [int(num) for num in str_arr]

def sum(arr, n):
	return(np.sum(arr))


n = len(arr)

result = sum(arr, n)

print("The sum of the array is ", result)