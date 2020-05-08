# Creating a function of nth Fibonacci number

n = int(input('Enter a number upto which you want the Fibonacci sequence :  '))

def Fibonacci(n):
	if n < 0:
		print("The input is not correct")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)


# Running the function for nth fibonacci number

for n in range(n):
	n = n+1
	print(Fibonacci(n))		