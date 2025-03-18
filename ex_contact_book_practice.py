def display_menu():
    print("""Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit
""")

def add_contact(contact_book):
    name = input("Enter name: ")  # Get input for name
    
    # Check if the contact already exists
    if name in contact_book:
        print("Contact already exists!")
        return
    
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    # Add new contact to the contact book
    contact_book[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully!")
    print(contact_book)

# Example usage:
some_book = {}  # Contact book should be a dictionary that holds multiple contacts
#add_contact(some_book)
#add_contact(some_book)

def view_contact(contact_book):
    name = input()  # Get input for name
    if name in contact_book:
        contact_details = contact_book[name]  # Get the nested dictionary
        print(f"Name: {name}")  # Print the name separately
        for key, value in contact_details.items():
            print(f"{key.capitalize()}: {value}")  # Capitalize key for formatting
    else:
        print('Contact not found!')

def view_contact2(contact_book):
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found!")


details = {"Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"}}


def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        email = input()
        address = input()

        if phone or email or address != "":
            contact_book[name] = {
                "phone": phone,
                "email": email,
                "address": address
                }
        print("Contact updated successfully!")
    
    else:
        print("Contact not found!")

def edit_contact2(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        email = input()
        address = input()

        if phone == '':
            phone = contact_book[name]['phone']
        if email == '':
            email = contact_book[name]['email']
        if address == '':
            address = contact_book[name]['address']

        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def delete_contact_2(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

    
def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for key, value in contact_book.items():
            print(f"Name: {key}")
            print(f"Phone: {value['phone']}")
            print(f"Email: {value['email']}")
            print(f"Address: {value['address']}")       
         
def list_all_contacts_2(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            print()  # Blank line between contacts for readability


# Contact book dictionary
contact_book = {}

# Main loop
while True:
    display_menu()
    choice = input()
    if choice == "1":
        add_contact(contact_book)
    elif choice == "2":
        view_contact(contact_book)
    elif choice == "3":
        edit_contact(contact_book)
    elif choice == "4":
        delete_contact(contact_book)
    elif choice == "5":
        list_all_contacts(contact_book)
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")





