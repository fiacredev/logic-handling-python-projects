import random

pd = "abcde47857fghijklmn#@$*@!"
number = int(input("enter the length of password:"))
a = random.sample(pd,number)
attachIt = "".join(a)
print("random password is: ",attachIt)