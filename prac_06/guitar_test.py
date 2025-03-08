"""
Estimated: 5 minutes
Actual: 8 minutes
"""

from prac_06.guitar import Guitar


def test():
    """Test for any undesired outputs."""
    gibson = Guitar(name="Gibson L-5 CES", year=1925)
    another_guitar = Guitar(name="Another Guitar", year=2016)
    test_function(gibson, "get_age", 100)
    test_function(another_guitar, "get_age", 9)
    test_function(gibson, "is_vintage", True)
    test_function(another_guitar, "is_vintage", False)


def test_function(guitar, function, expected):
    """Get the class object instance and desired function then display the returned output with expectation."""
    print(f"{guitar.name} {function}() - Expected {expected}. Got {getattr(guitar, function)()}")


test()
