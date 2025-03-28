"""
Estimated: 5 minutes
Actual: minutes
"""

from datetime import datetime

VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar instance.
        year: int, year when guitar was made
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate age from made year and current year."""
        current_year = datetime.now().year
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Return whether the guitar age more or equals to VINTAGE_AGE."""
        return self.get_age() >= VINTAGE_AGE
