# Number Guessing
# The computer picks a random number from 1-10, and you have 5 tries to guess it!

import random

randomnum = random.randint(1, 10)

user = int(input("Select a number from 1 to 10\n"))

for i in range(4):
    if user > randomnum:
        print("Too high. Try a smaller number!")
    elif user < randomnum:
        print("Too low. Try a bigger number!")
    else:
        print("You guessed the right number!")
        break
    user = int(input())
