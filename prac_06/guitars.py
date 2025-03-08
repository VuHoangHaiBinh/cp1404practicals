"""
Estimated: 15 minutes
Actual: 13 minutes
"""
from prac_06.guitar import Guitar


def main():
    """Repeatedly ask for guitar name, produced year and cost until blank is entered then display all guitars."""
    print("My guitars!")
    guitars = []

    # dummy data for testing
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512))

    name = input("Name: ").strip()
    while name != "":
        year = int(get_valid_number("Year: "))
        cost = get_valid_number("Cost: $")
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ").strip()

    print("\n... snip ...\n")
    print("These are my guitars:")
    display_guitars(guitars)


def get_valid_number(prompt):
    """Repeatedly validate input until it's a proper number."""
    is_valid = False
    number = float()

    while not is_valid:
        try:
            number = float(input(prompt))
            is_valid = True if number > 0 else print("Number must be > 0")
        except ValueError:
            print("Please enter a proper number")

    return number


def display_guitars(guitars):
    """Display all guitars in list in formatted form."""
    max_guitar_name_length = max(len(guitar.name) for guitar in guitars)
    max_guitar_cost_length = max(len(f"{guitar.cost:,.2f}") for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{max_guitar_name_length}} ({guitar.year}), worth ${guitar.cost:>{max_guitar_cost_length},.2f}{vintage_string}")


main()
