
str_arr = input().split()

arr = [int(num) for num in str_arr]

d = int(input('Enter a number by which you want to rotate an array : ' ))

n = int(input('Enter the size of the array : ' ))

# Function to left rotate an arr[] of size n by d

def leftRotate(arr, d, n):
	for i in range(d):
		leftRotateByOne(arr, n)


# Function to left Rotate arr[] of size n by 1

def leftRotateByOne(arr, n):
	temp = arr[0]
	for i in range(n-1):
		arr[i] = arr[i+1]
	arr[n-1] = temp


# print array and rotated array
leftRotate(arr, d, n)
print('The selected size {} rotated by {} is {}'.format(n, d, arr))

