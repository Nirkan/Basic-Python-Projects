
str_array = input().split(' ')

arr = [int(num) for num in str_array]

n = len(arr)


def max(arr, n):

	max = arr[0]

	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


Result = max(arr, n)

print("The biggest number in the given array is ", Result)