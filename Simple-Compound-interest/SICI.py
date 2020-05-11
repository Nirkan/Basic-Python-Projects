
p = float(input('Enter value of principal : '))
r = float(input('Enter value of rate : '))
t = float(input('Enter value of time : '))

def SI(p, r, t):

	SI = (p * r * t)/100
	return SI 



def CI(p, r, t):
	CI = p*(pow((1+r/100), t))
	return CI



print(SI(p, r, t))
print(CI(p, r, t))