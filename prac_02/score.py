"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
score = float(input("Enter score: "))
if score < 0 or score > 100:
    grade = "Invalid score"
elif score >= 90:
    grade = "Excellent"
elif score >= 50:
    grade = "Passable"
else:
    grade = "Bad"
print(grade)

