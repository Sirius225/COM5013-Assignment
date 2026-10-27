contacts = []

def add_contacts():
    name = input("Enter Contacts Name: ")
    number = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "number": number,
        "email": email
    }

    contacts.append(contact)
    print("Contact Details Have Been Added")

def main():
    print("Welcome To The Contacts App")
    add_contacts()


if __name__ == "__main__":
    main()
