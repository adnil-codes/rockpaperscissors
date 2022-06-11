from ast import Continue
import random
# from typing import Counter

counter = 0
# "R" for "rock",
# "P" for "paper",
# "S" for "scissors".
while counter <= 3:
    counter = counter + 1
    user_action = input("Enter one (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_selection = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_selection}")

    if user_action == computer_selection:
        print(" You both selected {user_action}. So its a tie")
    elif (user_action == "R" and computer_selection == "S") or (user_action == "P" and computer_selection == "R") or (user_action == "S" and computer_selection == "P"):
        print("You won")
    else:
        print("Computer wins")
        Continue
    if counter == 3:
        print("You have played 3 turns already")
    else:
        break
