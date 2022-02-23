import random

choices = ["rock", "paper", "scissors"]
Computer = random.choice("choices")
human = input("What do you pick, Rock, Paper or Scissors: ").lower()

if Computer == human:
    print("It's a tie the computer picked: " + Computer)
elif human == "rock":
    if Computer == "paper":
        print("You lost! The computer picked: " + Computer)

    if Computer == "scissor":
        print("You Won! the computer picked: " + Computer)
elif human == "paper":
    if Computer == "scissor":
        print("You lost! The computer picked: " + Computer)

    if Computer == "rock":
        print("You Won! the computer picked: " + Computer)

elif human == "scissor":
    if Computer == "paper":
        print("You Won! the computer picked: " + Computer)

    if Computer == "rock":
        print("You lost! The computer picked: " + Computer)
