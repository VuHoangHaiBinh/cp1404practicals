NUMBER_OF_PROMPTS = 5
USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """Let user input NUMBER_OF_PROMPTS numbers and display information about them and check if username has access"""
    numbers = []
    for i in range(NUMBER_OF_PROMPTS):
        number = int(input("Number: "))
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    username = input("Username: ")
    if username in USERNAMES:
        print("Access granted")
    else:
        print("Access denied")


main()
