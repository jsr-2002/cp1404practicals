"""
CP1404/CP5632 Practical
Taxi Simulator
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display taxis with index numbers."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Allow user to choose a taxi by index."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid input")
    return None


def drive_taxi(current_taxi):
    """Drive selected taxi and return cost."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0

    current_taxi.drive(distance)
    cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
    current_taxi.start_fare()
    return cost


def main():
    """The main taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    bill = 0.0

    print("Let's drive!")
    choice = ""

    while choice != "q":
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

        if choice == "c":
            selected = choose_taxi(taxis)
            if selected:
                current_taxi = selected

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill += drive_taxi(current_taxi)

        elif choice != "q":
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


main()
