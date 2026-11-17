contacts = [] #creates an empty list to store contacts

def add_contacts(): #this function will ask the user for the contact details and saves new contacts
    
    #asks the user to enter details 
    name = input("Enter Contacts Name: ")
    number = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    #stores details in a dictionary and each detail has a key name, number, and email
    contact = {
        "name": name,
        "number": number,
        "email": email
    }
    #adds the contacts disctionary to the contacts list
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

#this function runs the program
def main():

    #keeps the menu displayed until the user makes a choice
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")

        #asks the user to enter their choice
        choice = input("Enter your choice: ")

        #runs the relevant function based on the user's choice
        if choice == "1":
            add_contacts()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
