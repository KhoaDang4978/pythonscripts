# An inventory system for a small store
# Each item has a name, price, and quantity
# User can add items, update quantity, remove items, and show items that are low stock (quantity below 5)
# Saves everything to JSON.

# //--------------------------------------------------------------------------------------------------------//

print("This is an inventory system")
print("---------------------------")
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
import json
import os
items = []
if os.path.exists("inventory.json"):
    with open("inventory.json") as f:
        items = json.load(f)
while True:
    operation = str(input("Choose your operation (add items, update quantity, remove items, show low stock items or exit): "))
    if operation == "add items":
        name = str(input("Input item's name: "))
        price = str(input("Input item's price: $"))
        quantity = str(input("Input quantity: "))
        i = Item(name, price, quantity)
        items.append({
            "name": i.name,
            "price": i.price,
            "quantity": i.quantity
        })
        with open("inventory.json", 'w') as f:
            json.dump(items, f)
    elif operation == "update quantity":
        name = input("Which item's quantity do you want to update?")
        quantity = str(input("Updated quantity: "))
        for item in items:
            if item["name"] == name:
                item["quantity"] = quantity
        with open("inventory.json", "w") as f:
            json.dump(items, f)
    elif operation == "remove items":
        name = input("Which item do you want to remove?")
        for item in items:
            if item["name"] == name:
                items.remove(item)
        print("Item removed.")
        with open("inventory.json", "w") as f:
            json.dump(items, f)
    elif operation == "show low stock items":
        for item in items:
            if int(item["quantity"]) < 5:
                print(f"{item["name"]} - {item[quantity]} left.")
    elif operation == "exit":
        break
    else: 
        print("Invalid operation!")