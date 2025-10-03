"""Password Checker"""

import string

MIN_LENGTH = 8
MAX_LENGTH = 20
REQUIRE_SPECIAL_CHAR = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    password = get_password()
    print_stars(password)


def get_password():
    """Prompt user until they enter a valid password"""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, "
          f"and contain at least one uppercase, one lowercase, and one digit.")
    if REQUIRE_SPECIAL_CHAR:
        print("It must also contain at least one special character:", SPECIAL_CHARACTERS)

    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password")
        password = input("> ")
    return password


def is_valid_password(password):
    """Check if password is valid"""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if REQUIRE_SPECIAL_CHAR and not any(c in SPECIAL_CHARACTERS for c in password):
        return False
    return True


def print_stars(password):
    """Print stars same length as password"""
    print("*" * len(password))


main()
