# This is a shopping cart
print("Welcome to our store! This is your shopping cart.")
print("-------------------------------------------------")
total = 0
items = []
prices = []
while True:
    item = str(input("Please input the item you want to buy (or 'done' to finish): "))
    items.append(item)
    if item == "done":
        items.remove("done")
        print("Your receipt: ")
        for i in range(len(items)):
            print(f"{items[i]} - ${prices[i]}")
        print(f"Your total is: ${total}")
        break
    price = float(input(f"Please input the price of {item}: $"))
    prices.append(price)
    total += price
    print(f"{item} added to cart!")