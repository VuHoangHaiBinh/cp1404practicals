"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When either the input numerator or denominator is not a number
2. When will a ZeroDivisionError occur? When denominator is equal to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? OK
"""


def get_valid_denominator(prompt):
    denominator = int(input(prompt))
    while denominator == 0:
        print("Denominator must not be 0")
        denominator = int(input(prompt))
    return denominator


try:
    numerator = int(input("Enter the numerator: "))
    denominator = get_valid_denominator("Enter the denominator: ")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
