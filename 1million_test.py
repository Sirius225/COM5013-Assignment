
import json
import time

from main import ContactManager

#creates a separate test file, keeping your real contacts safe
test_filename = "test_contacts.json"

number_of_contacts = 1000000

print("Creating one million test contacts...")

#generates the contacts directly into the test JSON file
with open(test_filename, "w") as file:
    file.write("[")

    for i in range(number_of_contacts):

        contact = {
            "name": f"Contact{i}",
            "number": "07123456789",
            "email": f"contact{i}@example.com"
        }

        if i > 0:
            file.write(",")

        json.dump(contact, file)

    file.write("]")

print("Test contacts created successfully.")

#creates your actual ContactManager
manager = ContactManager()

#changes the filename so your real contacts are untouched
manager.filename = test_filename

#measures how long the actual loading function takes
start_time = time.perf_counter()

manager.load_contacts()

load_time = time.perf_counter() - start_time

#tests dictionary searching
search_name = "contact999999"

start_time = time.perf_counter()

result = manager.contact_lookup.get(search_name)

search_time = time.perf_counter() - start_time

#displays the results
print("Contacts loaded:", len(manager.contacts))
print("Dictionary entries:", len(manager.contact_lookup))
print("Loading time:", load_time, "seconds")
print("Search result:", result.name if result else "Not found")
print("Dictionary search time:", search_time, "seconds")
