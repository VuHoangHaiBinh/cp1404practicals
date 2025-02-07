MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """get valid user score and get user choice for determining grade or print asterisks until user exit"""
    score = get_valid_score()
    print(MENU)
    choice = input("Your choice: ").lower()
    while choice != 'q':
        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            grade = determine_grade(score)
            print("Your grade is:", grade)
        elif choice == 's':
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Your choice: ").lower()


def get_valid_score():
    """repeatedly validate user input score until it meets the requirement"""
    score = int(input("Your score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Your score: "))
    return score


def print_stars(score):
    """print a line of stars based on the score number"""
    print("*" * score)


def determine_grade(score):
    """determine grade from passed in score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    return "Bad"


main()
