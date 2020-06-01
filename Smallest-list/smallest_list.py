
print('Enter elements of the list seperated by single space')

str_list = input().split(' ')

list = [int(num) for num in str_list]

sml = list[0]

for ele in range(len(list)):
	if  list[ele] < sml:
		sml = list[ele]
	
print('The Smallest elements is : ', sml)


