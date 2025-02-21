import random

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
NUMBER_OF_RANDOM_NUMBERS = 6


def main():
    """Ask user for number of picks and display that many rows of 6 quick random numbers that are non-repeated and sorted"""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        random_numbers = generate_picks(NUMBER_OF_RANDOM_NUMBERS, MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        row_string = " ".join(f"{number:>{len(str(MAXIMUM_RANDOM_NUMBER))}}" for number in sorted(random_numbers))
        print(row_string)


def generate_picks(number, low_bound, high_bound):
    """Generate an array of number numbers with passed in low / high boundaries"""
    random_numbers = []
    for i in range(number):
        random_number = random.randint(low_bound, high_bound)
        while random_number in random_numbers:
            random_number = random.randint(low_bound, high_bound)
        random_numbers.append(random_number)
    return random_numbers


main()
