import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

count = int(input('Number of passwords : '))

length = int(input('Length of password : '))

for pwd in range(count):
	password = ' '
	for x in range(length):
		password += random.choice(chars)
	print(password)