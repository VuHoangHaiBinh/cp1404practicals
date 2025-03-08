"""
Estimated: 5 minutes
Actual: 5 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]
print("The dynamically typed languages are:")
print("\n".join(
    programming_language.name for programming_language in programming_languages if programming_language.is_dynamic()))
