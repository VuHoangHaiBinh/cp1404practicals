"""
Email
Estimate: 8 minutes
Actual:   7 minutes
"""

def main():
    """repeatedly ask for email until blank is input and extract name from email to display"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/n) ").lower().strip()
        if not choice == "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """extract name from passed in email using common email pattern"""
    name = " ".join(email.split("@")[0].split('.'))
    return name.title()


main()
