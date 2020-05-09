# input two numbers

N1 = input("First number: " )
N2 = input("Second number: " )

# Add the numbers

Sum = float(N1) + float(N2)

print("Sum of {} and {} is : {} ".format(N1,N2,Sum))



## Function Sum

def sum(n1, n2):
	sum = float(n1 + n2)
	return sum
