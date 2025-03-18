"""
Estimated: 5 minutes
Actual: 3 minutes
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage.
        typing: string, can be either Dynamic or Static
        reflection: boolean, shows whether the language is reflective or not
        year: int, year when language was published
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return whether the class typing is Dynamic or not."""
        return self.typing == "Dynamic"
