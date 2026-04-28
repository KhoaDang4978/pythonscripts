# This is a contact class for the phonebook
class Contact:
    def __init__(self, name, number):
        name = str(input("Please input contact's name: "))
        self.name = name
        number = input("Please input contact's number: ")
        self.number = number
    def display(self):
        print(f"Here's contact info: {self.name}: {self.number}")