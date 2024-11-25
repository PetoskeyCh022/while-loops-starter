# Charles
# 11/25/2024
# Number Guess Game with WHILE Loop

import random

name = input("Hello user, welcome to my guessing game. Before we start, what should I refer to you as?\n[Your name]: ").capitalize()
while name == "":
    name = input(f"Sorry, {name} is not a valid name. Please enter a valid name.\n[Your name]: ")
else:
    number = random.randint(1,100)
    print(f"Hi, {name}, I'm thinking of a number between 1 and 100")
    guessesTaken = 0

    while guessesTaken < 5:
        guess = int(input("Enter a guess:"))
        if guess < number:
            print("That guess was too low.")
            guessesTaken += 1
        elif guess > number:
            print("That guess was too high!")
            guessesTaken += 1
    else:
        if guess == number:
            print(f"Winner winner, chicken dinner! Congrats {name}, you guessed the correct number!")
        else:
            print(f"You lose, too bad. Better luck next time. The right number was {number}")
    

# if guess == number:
#     print(f"Winner winner, chicken dinner! Congrats {name}, you guessed the correct number!")
# else:
#     print(f"You lose, too bad. Better luck next time. The right number was {number}")