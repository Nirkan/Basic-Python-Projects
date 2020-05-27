print("Enter the numbers of the list seperated by only one space bar : ")

str_list = input().split(' ')

list = [int(num) for num in str_list]

print("The list is : ", list)

length = 0
for i in list:
	length = length + 1


print("Length of the list is : "+ str(length))
