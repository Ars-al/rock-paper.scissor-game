import random

computer_win = 0
user_win = 0
option = ["rock" , "paper" , "scissor"]

play = input("Do you want to play? ")
if play.lower() != "yes":
        quit()
else:
        print("Let's Play!")

while True:

    user_input = input("Type rock/paper/scissor or Q to quit! ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    computer_pick = option[random_number]
    print("Computer picked" , computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_win += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_win += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_win += 1

    else:
        print("You lost!")
        computer_win += 1

print("You won" , user_win , "times!")
print("Computer won" , computer_win , "times!")