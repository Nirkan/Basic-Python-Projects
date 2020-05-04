import random

number = random.randrange(1,26)

#print("The random number is: ", number)

guess = int(input("Guess the random number: "))


if guess == number:
	print("Wow! , You got it right")
elif guess < number:
	print("Sorry, your guess is low")
else:
	print("Sorry, your guess was high")

		