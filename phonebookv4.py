# This is a phonebook
print("Welcome to the phonebook!")
print("-------------------------")
phonebook = {}
import json
# Contact class
class Contact:
        def __init__(self, name, number):
            self.name = name
            self.number = number
        def display(self):
            print(f"Here's contact info: {self.name}: {self.number}")
        def update_number(self, new_number):
            self.number = new_number
import os
if os.path.exists("contact.txt"):
    with open("contact.txt") as f:
        print(f.read())
while True:
    operation = str(input("Please choose your operation (add contact, look up contact, delete contact, show all contact, export contacts, import contacts or exit): "))
    if operation == "add contact":
        name = str(input("Please input the contact's name: "))
        number = input("Please input contact number: ")
        c = Contact(name, number)
        phonebook[name] = c
        print("Contact added!")
    elif operation == "look up contact":
        z = str(input("Please input contact's name: "))
        if z in phonebook:
            phonebook[z].display()
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
            y.display()
    elif operation == "exit":
        print("Thank you for using the phonebook. Bye!")
        break
    elif operation == "export contacts":
        with open("contact.json", "w") as f:
            data = {}
            for name, contact in phonebook.items():
                data[name] = {"number": contact.number}
            json.dump(data, f)
    elif operation == "import contacts":
        with open("contact.json") as f:
            data = json.load(f)
            for name, info in data.items():
                phonebook[name] = Contact(name, info ["number"])
    else: 
        print("Invalid operation! Try again")