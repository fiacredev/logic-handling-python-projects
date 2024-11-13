import random

def printMain():
    print("i am with your POV")

def printOther():
    print(" f** with others first ")


def number_guessing_game():
    number_to_guess = random.randint(1,3)
    attempts = 0
    print("welcome to the number guessing game")
    print("i am thinking of number between 1 and 70")

    guess = int(input("make a guess"))
    attempts += 1
    if(guess) < number_to_guess:
        print("so low number provided")
    elif(guess)>number_to_guess:
        print("so high number provided")
    else:
        print(f"congratulations you have guessed number in {attempts} attempts")
      

if __name__ == "__main__":
    number_guessing_game()


# def number_guessing_game():
#     # deal with generation random number between 1 and 100
#     number_to_guess = random.randit(1,100)
#     # deal with initializing the number with attempts
#     attempts = 0
#     print("welcome to the number guessing game")
#     print("i am thinking of number of 1 and 100")

#     while True:
#         # deal with getting the user guess
#         guess = int(input("make aguess:"))
#         except ValueError:print("please enter a valid integer")
#         continue
#         attempts += 1
#         # lets deal with checkng the guess

#         if(guess) < number_to_guess:
#             print("too low number !")
#             else guess > number_to_guess:
#                 print("too high number !")
#                 else:print(f"congratulations! you have guessed the nums in {attempts} attempts")
#                 break
#                 # deal with running the game here
#                 if __name__ == "__main__":number_guessing_game()