
n = int(input("Enter a desired number to find its factorail : "))

def Factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		return n * Factorial(n-1)


print(Factorial(n))