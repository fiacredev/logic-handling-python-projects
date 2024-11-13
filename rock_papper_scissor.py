import random

emojis = { 'r':'⬛', 'p':'📃', 's':'✂'}
choices = ("r","p","s")

playing = True
while playing:
    user_choice = input("rock papper & scissors? (r/p/s): ").lower()

    if user_choice not in choices:
        print("invalid choice made!")
        continue

    computer_choice = random.choice(choices)

    print(f"you choose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Ahh Tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("now you win the game !!")
    else:
        print("you lose the game now !!")

    should_continue = input("contiue? (y/n): ").lower()

    if should_continue == 'n':
        break