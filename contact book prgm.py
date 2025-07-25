contacts={}
def add_contact():
    name=input("Enter name:")
    phone=input("Enter phone number:")
    contacts[name]=phone
    print("Contact added.\n")

def view_contacts():
    if not contacts:
        print("No contacts found./n")
        return
    print("\nContact list:")
    for name,phone in contacts.items():
        print(f"{name}:{phone}")
    print()

def search_contact():
    name=input("Enter name to search:")
    if name in contacts:
        print(f"Found: {name}-{contacts[name]}\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name=input("Enter name to delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted\n")
    else:
        print("Contact not found\n")

def main():
    while True:
        print("1.Add contact")
        print("2.View contact")
        print("3.Search contact")
        print("4.Delete contact")
        print("5.Exit")
        choice=input("Choose an option:")
        if choice=='1':
            add_contact()
        elif choice=='2':
            view_contacts()
        elif choice=='3':
            search_contact()
        elif choice=='4':
            delete_contact()
        elif choice=='5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")
if __name__ == "__main__":
    main()
