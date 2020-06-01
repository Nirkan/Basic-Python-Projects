
print('Enter elements of the list seperated by single space')

str_list = input().split(' ')

list = [int(num) for num in str_list]


sum = 0

for ele in range(0, len(list)):
	sum = sum + list[ele]


print('sum of all elemets of the list is : ', sum )