# code with modularization with refactoring

import random

emojis = { 'r':'⬛', 'p':'📃', 's':'✂'}
choices = ("r" , "p" , "s")

playing = True
def get_user_choice():
    while playing:
        user_choice = input("rock papper & scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("invalid choice made...")

def display_choices(user_choice,computer_choice):
    print(f"you choose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choice]}")

def determing_the_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        print("Ahh Tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("now you win the game !!")
    else:
        print("you lose the game now !!")

def play_game():
    while playing:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice,computer_choice)
        determing_the_winner(user_choice,computer_choice)

        should_continue = input("contiue? (y/n): ").lower()

        if should_continue == 'n':
            break

play_game()