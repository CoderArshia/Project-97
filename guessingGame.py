import random
chances = 0
number = random.randint(1,10)

print("Number Guessing Game")
print("Guess a number between 1 and 9")

while chances < 5:
    chances = chances+1
    guess = int(input("Enter your guess :- "))

    if guess < number:
        print("Your guess was too low")
    elif guess > number:
        print("Your guess was too high")
    else:
        print("congratulations, you won!!")
        break

    if not chances < 5:
        print("you lose, The number is", number)