
# Creating a list of desired range.

r = int(input('Enter a range for generating a list : '))

def list(r):
	list = []
	i = 0
	for i in range(r):
		if i%2 == 0:
			list.append(i)
		elif i%3 == 0:
			list.append(i)
	i = i + 1
	return list
	
print(list(r))


# Checking if the number belongs to the above list

N = int(input('Enter a number you want to check in the list : ' ))

for num in list(r):
	if num == N:
		print('Hurray! the number {} is in the list'.format(N))
		break
else:
		print('Sorry! the number {} is not found in the list'.format(N))
	

