PASSWORD_LENGTH = 10
password = len(input("Enter password: "))
while password <= PASSWORD_LENGTH:
    print("Invalid password")
    password = len(input("Enter password: "))
print("*" * password)
