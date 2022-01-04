import random
print("Number Guessing game")
number=random.randint(1,9)
chances = 0
while chances > 5:
    guess = int(input("Enter you guess:"))
    if guess == number:
        print("Congratulation you won")
        break

    if not chances > 5:
        print("You lose. The Number is: ",number)

