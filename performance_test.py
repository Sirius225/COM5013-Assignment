
import time

from main import Contact, ContactManager

# creates a contact manager
manager = ContactManager()

# number of contacts to generate
number_of_contacts = 1000000

# creates a large dataset
for i in range(number_of_contacts):
    name = f"Contact{i}"
    contact = Contact(name, "123456789", f"contact{i}@example.com")

    manager.contacts.append(contact)
    manager.contact_lookup[name.lower()] = contact


# name of the contact we want to find
search_name = "contact99999"

number_of_searches = 1000

# TEST 1: Dictionary search
start_time = time.perf_counter()

for i in range(number_of_searches):
    result = manager.contact_lookup.get(search_name)

dictionary_time = time.perf_counter() - start_time

# TEST 2: List linear search
start_time = time.perf_counter()

for i in range(number_of_searches):
    result = None

    # checks each contact until the matching name is found
    for contact in manager.contacts:
        if contact.name.lower() == search_name:
            result = contact
            break

list_time = time.perf_counter() - start_time

# displays the comparison
print("\n===== SEARCH PERFORMANCE RESULTS =====")
print("Number of contacts:", number_of_contacts)
print("Number of searches:", number_of_searches)
print("Dictionary search time:", dictionary_time, "seconds")
print("List search time:", list_time, "seconds")
print("Dictionary average:", dictionary_time / number_of_searches, "seconds")
print("List average:", list_time / number_of_searches, "seconds")
