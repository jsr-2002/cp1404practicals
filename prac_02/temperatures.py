"""Temperature conversion program with functions."""


def main():
    """Convert temperatures using a menu."""
    MENU = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {fahrenheit_to_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


main()
