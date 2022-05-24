import random

x = random.randint(1,3)  # gets a random number
user_action = input("Get input")  # gets input from user

choices = ["rock", "paper", "scissors"]  # this is a list

computer_action = x

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == 1:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == 2:
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == 3:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")