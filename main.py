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

    #this function asks the user for contact details and saves new contacts
    def add_contacts(self):

        #asks the user to enter contact details
        name = input("Enter Contacts Name: ").strip()
        number = input("Enter Phone Number: ").strip()
        email = input("Enter Email: ").strip()

        #checks that none of the fields are empty
        if not name or not number or not email:
            print("All fields are required. Please try again.")
            return

        #checks the dictionary for an existing contact with this name
        if name.lower() in self.contact_lookup:
            print("Contact with this name already exists.")
            return

        #creates a new contact object
        contact = Contact(name, number, email)

        #adds the new contact to the list
        self.contacts.append(contact)

        #adds the new contact to the dictionary
        self.contact_lookup[name.lower()] = contact

        #saves the contact details to the JSON file
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

   # this function searches for a contact using the dictionary
    def search_contact(self):

        # asks the user to enter the name they want to find
        search_name = input("Enter the name that you would like to search for: ").strip()

        # searches the dictionary using the contact name
        contact = self.contact_lookup.get(search_name.lower())

        # checks whether the contact exists
        if contact:

            print("\nName:", contact.name)
            print("Number:", contact.number)
            print("Email:", contact.email)

        else:
            print("Contact not found.")


    #this function allows the user to edit an existing contact
    def edit_contacts(self):

        #asks which contact the user wants to edit
        search_name = input("Enter the name of the contact you would like to edit: ").strip()

        #finds the contact directly using the dictionary
        contact = self.contact_lookup.get(search_name.lower())

        #checks whether the contact exists
        if contact is None:
            print("Contact not found.")
            return

        print("Leave a field blank if you would like to keep the current detail.")

        #asks for updated details
        new_name = input("Enter new name: ").strip()
        new_number = input("Enter new number: ").strip()
        new_email = input("Enter new email: ").strip()

        #checks whether the new name is already being used
        if new_name:
            if new_name.lower() in self.contact_lookup and new_name.lower() != search_name.lower():
                print("Another contact already uses this name.")
                return

            contact.name = new_name

        #updates only the fields that have new details
        if new_number:
            contact.number = new_number

        if new_email:
            contact.email = new_email

        #removes the old name from the dictionary
        self.contact_lookup.pop(search_name.lower(), None)

        #adds the updated name to the dictionary
        self.contact_lookup[contact.name.lower()] = contact

        #saves the updated contact details
        self.save_contacts()

        print("Contact details have been updated.")


        #displays a message if the contact was not found
        print("Contact not found.")

 
    #this function allows the user to delete a contact
    def delete_contact(self):

        #asks which contact the user wants to delete
        search_name = input("Enter the name of the contact that you would like to delete: ").strip()

        #finds the contact directly using the dictionary
        contact = self.contact_lookup.get(search_name.lower())

        #checks whether the contact exists
        if contact is None:
            print("Contact not found.")
            return

        #removes the contact from the list
        self.contacts.remove(contact)

        #removes the contact from the dictionary
        self.contact_lookup.pop(search_name.lower(), None)

        #saves the updated contact details
        self.save_contacts()

        print("Contact has been deleted.")


# this function runs the program
def main():

    # creates a ContactManager object to manage all contacts
    manager = ContactManager()
    manager.load_contacts()
    # keeps the menu displayed until the user makes a choice
    while True:

        print("Contacts Management App")
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

