PASSWORD_LENGTH = 10


def main():
    """ask user for valid password and print a line of asterisks"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """get password that is longer than required password length"""
    password = input("Enter password: ")
    while len(password) <= PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """print a line of asterisk based on the length of password"""
    print("*" * len(password))


main()
