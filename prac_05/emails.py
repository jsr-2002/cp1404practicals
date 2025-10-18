"""
Emails - Map email to person name
Estimate: 30 minutes
Actual:   TODO
"""

def extract_name_from_email(email: str) -> str:
    """
    Extract a plausible name from an email like "john.smith99@example.com" -> "John Smith99"
    """
    local = email.split("@", 1)[0]
    parts = local.replace(".", " ").replace("_", " ").split()
    if not parts:
        return ""
    return " ".join(p.capitalize() for p in parts)


def main():
    email_to_name = {}

    while True:
        email = input("Email: ").strip()
        if email == "":
            break

        suggested_name = extract_name_from_email(email)
        # Default Yes behaviour (press Enter to accept)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
        if confirmation not in {"", "y", "yes"}:
            name = input("Name: ").strip().title()
        else:
            name = suggested_name

        email_to_name[email] = name

    # Display entries
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
