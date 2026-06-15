contacts = []
while True:
    print("\n==== CONTACT BOOK ====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        contact = {"name": name,
                   "phone": phone,
                   "email": email,
                   "address": address
                  }
        contacts.append(contact)
        print("Contact added successfully!")
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n---- Contact List ----")
            for i in range(len(contacts)):
                print(f"\nContact {i + 1}")
                print("Name :",contacts[i]["name"])
                print("Phone :",contacts[i]["phone"])
                print("Email :",contacts[i]["email"])
                print("Address:",contacts[i]["address"])
    elif choice == "3":
        search = input("Enter Name or Phone Number:")
        found = False
        for contact in contacts:
            if search == contact["name"] or search == contact["phone"]:
                print("\nContact Found")
                print("Name :",contact["name"])
                print("Phone :",contact["phone"])
                print("Email :",contact["email"])
                print("Address :",contact["address"])
                found = True
        if not found:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter contact name to update: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("Enter New Phone Number:")
                contact["email"] = input("Enter New Email: ")
                contact["address"] = input("Enter New Address: ")
                print("Contact updated successfully!")
                found = True
                break
        if not found:
            print("Contact not found.")
    elif choice == "5":
        name = input("Enter contact name to delete: ")
        found = False
        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break
        if not found:
            print("Contact not found.")
    elif choice == "6":
        print("Thank You For Using Contact Book!")
        break
    else:
        print("Invalid choice.Pleaes try again.")