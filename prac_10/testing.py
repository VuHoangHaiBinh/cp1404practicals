"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest

from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join(s for _ in range(n))


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def convert_to_sentence(phrase):
    """
    Convert a phrase into a sentence.
    >>> convert_to_sentence("hello")
    'Hello.'
    >>> convert_to_sentence("hi there")
    'Hi there.'
    >>> convert_to_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> convert_to_sentence("   ")
    ''
    """
    sentence = phrase.strip().capitalize()

    if sentence != "" and sentence[-1] != ".":
        sentence += "."

    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # CASE 1: with parameter
    car = Car(fuel=10)
    assert car.fuel == 10, "Expected: fuel = 10"

    # CASE 2: no parameter
    car = Car()
    assert car.fuel == 0, "Expected: fuel = 0"


run_tests()

doctest.testmod()
