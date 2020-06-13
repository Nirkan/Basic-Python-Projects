
import math

n = int(input("Enter a number : "))


prime = []

for i in range(2, n+1):
	prime.append(i)



i = 2

# from i = 2 to sqrt(n)

while (i <= int(math.sqrt(n))):

	# if i is in the list
	# we need to delete its multiples

	if i in prime:

		for j in range(i*2, n+1, i):

			if j in prime:

				prime.remove(j)

	i = i + 1


print("The list of prime number is : ", prime)