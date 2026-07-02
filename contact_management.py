contacts = {}

while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print("Contact added successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, info in contacts.items():
                print(f"Name: {name}")
                print(f"Phone: {info['Phone']}")
                print(f"Email: {info['Email']}")
                print("-----------------------")

    elif choice == "3":
        name = input("Enter the contact name to edit: ")
        if name in contacts:
            phone = input("Enter New Phone Number: ")
            email = input("Enter New Email: ")
            contacts[name] = {"Phone": phone, "Email": email}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
