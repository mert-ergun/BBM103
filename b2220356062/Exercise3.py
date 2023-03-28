import random

number = random.randint(1, 25)

print("Guess a number between 1 and 25")

guess = int(input("Enter a number:"))

while True:
    if guess == number:
        print("You Won!")
        exit()
    elif guess < number:
        print("Increase your number!")
        guess = int(input("Enter a number:"))
    elif guess > number:
        print("Decrease your number!")
        guess = int(input("Enter a number:"))
