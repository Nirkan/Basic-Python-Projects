
str_arr = input().split(' ')

arr = [int(num) for num in str_arr]

def Monotonic(arr):
	monotonic = all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
	Nmonotonic = all(arr[i] >= arr[i+1] for i in range(len(arr) - 1))

	return (monotonic or Nmonotonic)



print(Monotonic(arr))