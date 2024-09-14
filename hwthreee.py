contacts = []

def display_contacts():
    if not contacts:
        print('Contacts list is empty')
    else:
        for index, contact in enumerate(contacts):
            print(f'{index + 1}.{contact}')

def add_contact():
    name = input(print('Enter contact name: '))
    number = input(print('Enter number of the contact: '))
    contact = f'{name} - {number}'

    contacts.append(contact)
    print(contact + 'is successfully added to the database!')



def edit_contact():
    display_contacts()
    if contacts:
        index = int(input('Enter the number of contact to change: ')) - 1
        if 0 < index < len(contacts):
            new_name = input('Enter new name: ')
            new_phone = input('Enter new phone: ')
            contacts[index] = f'{new_name} - {new_phone}'
            print('Contacts edited')
        else:
            print('Wrong contact index!')


def delete_contact():
    display_contacts()
    if contacts:
        index = int(input('Enter the number of contact to change: ')) - 1
        if 0 < index < len(contacts):
            removed_contact = contacts.pop(index)
            print(f"Contact '{removed_contact} 'is removed")
        else:
            print('Wrong contact index!')

def main():
    while True:
        print("\nSelect action:")
        print("1. Display contacts")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter action index: ")

        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Wrong input. Try again!")


if __name__ == "__main__":
    main()

