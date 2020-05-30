
print("Enter elements of the list seperated by single space ")

str_list = input().split(' ')

list = [int(num) for num in str_list]

x = int(input("Enter the integer you want to count in the list : "))

def count(list, x):
	count = 0
	for e in list:
		if (e == x):
			count = count + 1
	return count

print('The number {} occurs {} times in the list'.format(x, count(list, x)))
