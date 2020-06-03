
L = input('Enter a string : ')


def Palindrome(L):
	if L == L[::-1]:
		print('The letter {} is palindromic.'.format(L))
	else:
		print('Sorry, letter {} is not palindromic.'. format(L))


Palindrome(L)