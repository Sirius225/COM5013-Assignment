contacts = [] #creates an empty list to store contacts

#this function will ask the user for the contact details and saves new contacts
def add_contacts(): 

    #asks the user to enter details 
    name = input("Enter Contacts Name: ").strip()
    number = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    #checks that none of the fields are empty
    if not name or not number or not email:
        print("All fields are required. Please Try again.")
        return


    #checks if a contact already exists with the same name
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact with this name already exists.")
            return


    #stores details in a dictionary and each detail has a key name, number, and email
    contact = {
        "name": name,
        "number": number,
        "email": email
    }
    #adds the new contact to the contact list
    contacts.append(contact)
    print("Contact Details Have Been Added")

def view_contacts(): #this function displays the saved contacts in the list


    if not contacts:
        print("No contacts have been saved yet")
        return 
        #this will stop the function if there are not contacts
    
    for contact in contacts:

        print("Name: ", contact["name"])
        print("Number: ", contact["number"])
        print("Email: ", contact["email"])
    #this display each piece of information

#this function searches for a contact using their name
def search_contact():

    #asks the user to enter the name they want to look for
    search_name = input("Enter the name that you would like to search for:").strip()

    #keeps track of whether a contact was found or not
    found = False

    #checks contacts in the contact list
    for contact in contacts:

        #compares names without having to worry about capital letters
        if search_name.lower() in contact["name"].lower():

            print("Name", contact["name"])
            print("Number", contact["number"])
            print("Email", contact["email"])

            found = True
    #displays a message if the contact was not found
    if not found:
        print("Contact not found.")

def edit_contacts(): #this function allows the user to edit an existing contact


    #asks which contact detail the user wants to edit
    search_name = input("Enter the name of the contact you would like to edit:").strip()

    for contact in contacts:

        if contact["name"].lower() == search_name.lower():

            print("Leave a field blank if you would like to keep the current detail.")

            #asks for updated details
            new_name = input("Enter new name: ").strip()
            new_number = input("Enter new number: ").strip()
            new_email = input("Enter new email: ").strip()


            #updates only the fields that habe new details
            if new_name:
                contact["name"] = new_name
            if new_number:
                contact["number"] = new_number
            if new_email:
                contact["email"] = new_email
                
            print("Contact details have been updated.")
            return
        
print("Contact not found.")

#this function will allow the user to delete a contact from the list
def delete_contact(): 

    #asks the user to enter the name of the contact they want to delete
    search_name = input("Enter the name of the contact that you would like to delete: ").strip()

    for contact in contacts:
        #runs a check to see if the name matches 
        if contact["name"].lower() == search_name.lower():

            #removes the matching name from the contact list
            contacts.remove(contact)
            print("Contact has been deleted.")
            return

    print("Contact not found.")





#this function runs the program
def main():

    #keeps the menu displayed until the user makes a choice
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")
        #asks the user to enter their choice
        choice = input("Enter your choice: ")

        #runs the relevant function based on the user's choice
        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            edit_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
