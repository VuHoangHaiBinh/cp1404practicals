from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars data and ask user to insert more then write back to file."""
    guitars = read_guitars(FILENAME)

    print(f"Imported {len(guitars)} from {FILENAME}")

    print("=== Insert your new guitars below here ===")
    name = input("Guitar name: ").strip()
    while name != "":
        year = int(get_valid_number("Year: "))
        cost = get_valid_number("Cost: $")
        guitars.append(Guitar(name, year, cost))
        name = input("Guitar name: ").strip()

    guitars.sort()
    print("These are your current guitars:")
    for guitar in guitars:
        print(guitar)

    write_guitars(FILENAME, guitars)
    print(f"Wrote {len(guitars)} guitars to {FILENAME}")


def test():
    """Test the program features for bugs."""
    number1 = get_valid_number("Insert number: ")  # Expect: 'a' -> retry
    number2 = get_valid_number("Insert number: ")  # Expect: 0 or -1 -> retry
    print(number1, number2)

    filename = "test.csv"
    guitars = [Guitar("1", 1, 1), Guitar("2", 1, 1)]
    write_guitars("test.csv", guitars)  # Expect: test.csv with 1,1,1 and 2,1,1

    guitars = read_guitars(filename)  # Expect: 2 Guitar objects (1,1,1) and (2,1,1)
    for guitar in guitars:
        print(guitar)


def read_guitars(filename):
    """Read from filename and initialize Guitar objects with data."""
    guitars = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parameters = line.strip().split(',')
            guitars.append(Guitar(parameters[0], int(parameters[1]), float(parameters[2])))
    return guitars


def write_guitars(filename, guitars):
    """Open filename to write all guitars from list."""
    with open(filename, 'w') as file:
        file.writelines(f"{guitar.name},{guitar.year},{guitar.cost}\n" for guitar in guitars)


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


if __name__ == "__main__":
    main()
    # test()
