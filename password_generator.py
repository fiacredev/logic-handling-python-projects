import random
import string

def generate_password():
    # combining aphabet(upper and lower). number and special character
    characters = string.ascii_letters + string.digits + string.punctuation
    number = int(input("enter the number of characters to be generated.."))
    # randomly selecting number of characters
    password = random.sample(characters,number)
    attachIt = "".join(password)
    print("random password is: ",attachIt)

password = generate_password()
print(password)