# This is a phonebook
print("Welcome to the phonebook!")
print("-------------------------")
phonebook = {}
while True:
    operation = str(input("Please choose your operation (add contact, look up contact, delete contact, show all contact or exit): "))
    if operation == "add contact":
        m = str(input("Please input the contact's name: "))
        n = input("Please input contact number: ")
        phonebook.update({(m): (n)})
        print("Contact added!")
    elif operation == "look up contact":
        z = str(input("Please input contact's name: "))
        if z in phonebook:
            print(f"Here's contact number: {phonebook[z]}")
        else:
            print("Contact not found!")
    elif operation == "delete contact":
        a = str(input("Please input the contact's name you want to delete: "))
        if a in phonebook:
            phonebook.pop(a)
            print("Contact deleted.")
        else: 
            print("Contact already doesn't exist. Try again.")
    elif operation == "show all contact":
        for x, y in phonebook.items():
            print(f"{x}: {y}")
    elif operation == "exit":
        print("Thank you for using the phonebook. Bye!")
        break
    else: 
        print("Invalid operation! Try again")