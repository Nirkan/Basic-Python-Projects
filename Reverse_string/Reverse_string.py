
S = input('Enter a string : ')

def Reverse(S):

	words = S.split(' ')

	for i in range(len(words)):
	      index = (len(words) - 1) - i
	      i = i + 1
	      print(words[index], end = ' ')


Reverse(S)