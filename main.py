import json
# this class is used for creating contacts
class Contact:

    # this sets up the details for each new contact
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

# this class will manage all contacts in the app
class ContactManager:

    # this will initialise an empty list to store contacts
    def __init__(self):
        self.contacts = []
        self.contact_lookup = {}
        self.filename = "contacts.json"
    
    #this function will save all contacts into a json file
    def save_contacts(self):
        data = []

        #converts each Contact object into a dictionary and adds it to the data list
        for contact in self.contacts:
            data.append({
                "name": contact.name,
                "number": contact.number,
                "email": contact.email
            })
        #this will write the contact details into the file    
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    #this function will load the contacts saved in the json file when the app starts        
    def load_contacts(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.contacts = []

            #this will convert each saved dictionary back into a Contact Object
            for item in data:
                contact = Contact(
                    item["name"],
                    item["number"],
                    item["email"]

                )
                self.contacts.append(contact)

                #adds the contact to the dictionary using the name as a key
                self.contact_lookup[contact.name.lower()] = contact

        except FileNotFoundError:

            #if the file does not exist, start with an empty contact list
            self.contacts = []
    # this function will ask the user for contact details and save new contacts
    def add_contacts(self):

        # asks the user to enter details
        name = input("Enter Contacts Name: ").strip()
        number = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()

        # checks that none of the fields are empty
        if not name or not number or not email:
            print("All fields are required. Please try again.")
            return

        # checks if a contact already exists with the same name
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("Contact with this name already exists.")
                return

        # creates a new contact object with the provided details
        contact = Contact(name, number, email)

        # adds the new contact to the contact list
        self.contacts.append(contact)
        #adds the new contact to the dictionary
        self.contact_lookup[name.lower()] = contact
        #saves the contact details to the json file
        self.save_contacts()

        print("Contact Details Have Been Added")

    # this function displays the saved contacts in the list
    def view_contacts(self):

        # checks whether the contacts list is empty
        if not self.contacts:
            print("No contacts have been saved yet.")
            return

        # goes through each contact in the list
        for contact in self.contacts:
            print("\nName:", contact.name)
            print("Number:", contact.number)
            print("Email:", contact.email)

        # this displays each piece of information

    # this function searches for a contact using their name
    def search_contact(self):

        # asks the user to enter the name they want to look for
        search_name = input("Enter the name that you would like to search for: ").strip()

        # keeps track of whether a contact was found or not
        found = False

        # checks contacts in the contact list
        for contact in self.contacts:

            # compares names without worrying about capital letters
            if search_name.lower() in contact.name.lower():

                print("\nName:", contact.name)
                print("Number:", contact.number)
                print("Email:", contact.email)

                found = True

        # displays a message if the contact was not found
        if not found:
            print("Contact not found.")

    # this function allows the user to edit an existing contact
    def edit_contacts(self):

        # asks which contact the user wants to edit
        search_name = input("Enter the name of the contact you would like to edit: ").strip()

        # checks each contact in the list
        for contact in self.contacts:

            if contact.name.lower() == search_name.lower():

                print("Leave a field blank if you would like to keep the current detail.")

                # asks for updated details
                new_name = input("Enter new name: ").strip()
                new_number = input("Enter new number: ").strip()
                new_email = input("Enter new email: ").strip()

                # checks whether the new name is already being used
                if new_name:
                    for other_contact in self.contacts:
                        if other_contact is not contact and other_contact.name.lower() == new_name.lower():
                            print("Another contact already uses this name.")
                            return

                    contact.name = new_name

                # updates only the fields that have new details
                if new_number:
                    contact.number = new_number

                if new_email:
                    contact.email = new_email

                #removes the old details from the dictionary
                self.contact_lookup.pop(search_name.lower(), None)

                #adds the updates contact details to the dictionary
                self.contact_lookup[contact.name.lower()] = contact

                # saves the updated contact details to the json file
                self.save_contacts()

                print("Contact details have been updated.")
                return

        # displays a message if the contact was not found
        print("Contact not found.")

    # this function will allow the user to delete a contact from the list
    def delete_contact(self):

        # asks the user to enter the name of the contact they want to delete
        search_name = input("Enter the name of the contact that you would like to delete: ").strip()

        # checks each contact in the list
        for contact in self.contacts:

            # runs a check to see if the name matches
            if contact.name.lower() == search_name.lower():

                # removes the matching contact from the contact list and updates the json file
                self.contacts.remove(contact)

                self.contact_lookup.pop(search_name.lower(), None)
                
                self.save_contacts()

                print("Contact has been deleted.")
                return

        print("Contact not found.")


# this function runs the program
def main():

    # creates a ContactManager object to manage all contacts
    manager = ContactManager()
    manager.load_contacts()
    # keeps the menu displayed until the user makes a choice
    while True:

        print("CONTACTS MANAGEMENT APP")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        # asks the user to enter their choice
        choice = input("Enter your choice: ")

        # runs the relevant function based on the user's choice
        if choice == "1":
            manager.add_contacts()

        elif choice == "2":
            manager.view_contacts()

        elif choice == "3":
            manager.search_contact()

        elif choice == "4":
            manager.edit_contacts()

        elif choice == "5":
            manager.delete_contact()

        elif choice == "6":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

