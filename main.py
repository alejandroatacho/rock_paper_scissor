import random

answer = input("What do you choose Rock, Paper or Scissor?: ")
# answer = answer.lower()
answer_bot = ["rock", "paper", "scissor"]
randnumber = random.randint(0, 2)

if answer_bot[randnumber] == answer:
    print("It's a tie!")
elif len(answer) == len(answer_bot[randnumber]):
    print("You won!")
else:
    print("You lost!")
