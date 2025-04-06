# TODO: The user should be able to choose from a list of available taxis,
# They can choose how far they want to drive,
# TODO: At the end of each trip, show them the trip cost and add it to their bill.
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Taxi simulation program that repeatedly ask user to choose / drive taxi and calcaulate bill."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
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


if __name__ == "__main__":
    main()
