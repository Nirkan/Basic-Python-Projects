
str_array = input('Enter elements of an array seperated by single space : ').split(' ')

arr = [int(num) for num in str_array]

low = 0

high = len(arr) - 1

x = int(input("Enter a value to search in the array : " ))


def binary_search(arr, low, high, x): 

	if high >= low:

		mid = (high + low) // 2

		# If the element is present in the middle itself

		if arr[mid] == x:
			return mid


		# If element is smaller than mid, then it should be in the left subarray

		elif arr[mid] > x : 
			return binary_search(arr, low, mid - 1, x)


		# If the element is on the right side of the array i.e. right subarray

		else:
			return binary_search(arr, mid + 1, high, x)


	# If the element is not present in the array

	else:
		print("Sorry ! we did not find the number")




print("The location of seared value in the array is : ", binary_search(arr, low, high, x)) 

