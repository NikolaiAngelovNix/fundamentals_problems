given_contact = input()
contacts_dict = {}

while "-" in given_contact:
    name, number = given_contact.split("-")
    contacts_dict[name] = number
    given_contact = input()

number_of_searches = int(given_contact)

for _ in range(number_of_searches):
    searched_name = input()
    if searched_name in contacts_dict:
        print(f"{searched_name} -> {contacts_dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
