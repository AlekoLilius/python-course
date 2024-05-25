import re

contacts = {}
phone_numbers = {}
emails = {}

def list_contacts():
    print(f"\n      ::: List Contacts :::\n")

    for name in contacts:
        print(
    f'''{name}
Phone Number: {phone_numbers[name]}
Email: {emails[name]}
Address: {contacts[name][0]}
Date of Birth: {contacts[name][1]}
    ''')

def search_contact():
    print(f"\n      ::: Search Contact :::\n")
    search_results = []
    search = input("Search: ")
    for contact in contacts:
        if search in contact.lower():
            search_results.append(contact)
    
    print(f"\n      ::: Search List :::\n")
    for result in search_results:
        print(result)

def get_additional_inputs():
    phone_number, email, address, date_of_birth = '', '', '', ''
    while True:
        phone_number = input("Phone Number (ex. 0701234567), press enter to skip: ")
        if phone_number.isdigit() and len(phone_number) == 10 or phone_number == '':
            break
        print("\nWrong format!\n")
    while True:
        email = input("Email (ex. name@gmail.com), press enter to skip: ")
        if re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+@(g|hot)mail\.com$", email) or email == '':
            break
        print("\nWrong format!\n")
    while True:
        address = input("Enter address (Street 11), press enter to skip: ")
        if re.match(r"^[A-Z]+[a-z]+\s[0-9]+$", address) or address == '':
            break
        print("\nWrong format!\n")
    while True:
        date_of_birth = input("Enter date of birth (2024-05-22), press enter to skip: ")
        if re.match(r"^(?:(?:19|20)\d{2})-(?:(?:0[1-9]|1[0-2]))-(?:(?:0[1-9]|[12]\d|3[01]))$", date_of_birth) or date_of_birth == '':
            break
        print("\nWrong format!\n")
    
    return phone_number, email, address, date_of_birth

def add_contact():
    print(f"\n      ::: Add Contact :::\n")
    name = ''
    while True:
        first_name = input("First Name: ")
        last_name = input("Last Name, press enter to skip: ")
        if first_name.isalpha() and last_name.isalpha() or first_name.isalpha() and last_name == '':
            if last_name.isalpha():
                name = first_name + ' ' + last_name
                break
            else:
                name = first_name
                break
        else:
            print("\nWrong format!\n")
    
    if name in contacts:
        print("\nContact Already Exists.\n")
        return
    
    additional_info = input("Do you want to add additional info? (y/n): ")

    phone_number, email, address, date_of_birth = '', '', '', ''
    if additional_info == 'y':
        phone_number, email, address, date_of_birth = get_additional_inputs()

    if input("Add Contact? (y/n): ") == 'y':
        contacts[name] = (address, date_of_birth)
        phone_numbers[name] = phone_number
        emails[name] = email
        print("Contact Added")
    else:
        print("No new contact added")
            

def update_contact():
    print(f"\n      ::: Update Contact :::\n")
    name = input("Full name of the contact to update: ")
    if name in contacts:
        phone_number, email, address, date_of_birth = get_additional_inputs()
        if input("Update Contact? (y/n): ") == 'y':
            contacts[name] = (address, date_of_birth)
            phone_numbers[name] = phone_number
            emails[name] = email
            print(f"{name} updated")
        else:
            print(f"{name} not updated")
    else:
        print(f"{name} not in list.")
            

def remove_contact():
    print(f"\n      ::: Remove Contact :::\n")
    name = input("Full name of the contact to remove: ")
    if name in contacts:
        if input("Are you sure? (y/n): "):
            del contacts[name]
            del phone_numbers[name]
            del emails[name]
            print(f"{name} removed from list.")
    else:
        print("Contact not in list.")

def main():

    print('''
::::::::::::::::::::::::::::::::
::: Contact Book Application :::
::::::::::::::::::::::::::::::::''')

    valid_actions = '123456'
    while True:
        print('''
      :::        Menu        :::
      ::: 1. List Contacts   :::
      ::: 2. Search Contact  :::
      ::: 3. Add Contact     :::
      ::: 4. Update Contact  :::
      ::: 5. Remove Contact  :::
      ::: 6. Exit Program    :::
              ''')
        
        action = input("Choose Action: ")
        if action not in valid_actions:
            print("\n        === Invalid Action ===")
            continue

        match action:
            case '1' : list_contacts()
            case '2' : search_contact()
            case '3' : add_contact()
            case '4' : update_contact()
            case '5' : remove_contact()
            case '6' : break

if __name__ == '__main__':
    main()