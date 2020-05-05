from random import randint

options = ['rock','paper','scissors']

random  = options[randint(0, 2)]

guess = input("Your choice inside ' ' is:  ").lower()

print("random mixing result: " , random)

if guess == random:
	print("Ah! Its a draw")
elif guess == "rock" and random == "paper":
	print("Sorry, you lost.")
elif guess == "rock" and random == "scissors":
	print("Hurray!, you won.")
elif guess == "scissors" and random == "paper":
	print("Hurray!, you won.")
elif guess == "scissors" and random == "rock":
	print("Sorry, you lost")
elif guess == "paper" and random == "rock":
	print("Hurray!, you won.")
elif guess == "paper" and random == "scissors":
	print("Sorry, you lost.")
