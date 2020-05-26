
print("Enter the numbers of the list seperated by only one space bar : ")

str_list = input().split(' ')

list = [int(num) for num in str_list]

def Slist(list):
	
	list[0], list[-1] = list[-1], list[0]

	return list


print("The list is : ", list)
print("The swapped list is : ", Slist(list))