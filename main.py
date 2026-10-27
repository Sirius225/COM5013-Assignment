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
    print("Welcome To The Contacts App")
    add_contacts() #runs function that adds contacts
    view_contacts() # runs function that displays the contacts

if __name__ == "__main__":
    main()
