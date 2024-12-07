# here you have to enter your email
email = input("enter you email: ")
index = email.index("@")
username = email[:index]
domain = email[index + 1:]

print(f"your username is {username} your domain is {domain}")