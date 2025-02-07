"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """get user score and print the determined grade"""
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print("Your grade is:", grade)


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
