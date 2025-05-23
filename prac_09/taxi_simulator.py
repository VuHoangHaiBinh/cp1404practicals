from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulation program that repeatedly ask user to choose, drive, and calculate fare for taxi."""
    current_taxi = None
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0

    print("Let's drive!")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            current_taxi = choose_taxi("Choose taxi: ", taxis)

        elif choice == "d":
            if current_taxi:
                price = drive_taxi(current_taxi)
                print(f"Your {current_taxi.name} cost you ${price:.2f}")
                bill += price
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all taxi objects in taxis list with index."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {str(taxi)}")


def get_valid_number(prompt, lower_bound=None, upper_bound=None):
    """Repeatedly ask for a valid number based on passed in parameters until satisfied."""
    is_valid = False
    valid_number = None
    while not is_valid:
        try:
            number = int(input(prompt))
            if lower_bound is not None and number < lower_bound:
                print("Number must be bigger than " + str(lower_bound))
            elif upper_bound is not None and number > upper_bound:
                print("Number must be smaller than " + str(upper_bound))
            else:
                valid_number = number
                is_valid = True
        except ValueError:
            print("Please enter a valid number!!")
    return valid_number


def choose_taxi(prompt, taxis):
    """Ask for taxi choice and validate if the object is accessible."""
    try:
        choice = get_valid_number(prompt)
        chosen_taxi = taxis[choice]
        return chosen_taxi
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(taxi):
    """Ask for distance, reset last trip distance then drive and get the price after."""
    distance = get_valid_number("Drive how far? ", lower_bound=0)
    taxi.start_fare()
    taxi.drive(distance)
    price = taxi.get_fare()
    return price


if __name__ == "__main__":
    main()
