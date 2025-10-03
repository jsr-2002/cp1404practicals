"""Password check program with functions."""


def main():
    """Get a password and display it as asterisks."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get a valid password from the user."""
    password = input("Enter a password: ")
    while len(password) < 5:  # Example rule: min 5 chars
        print("Password too short!")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print as many asterisks as the length of the password."""
    print("*" * len(password))


main()
