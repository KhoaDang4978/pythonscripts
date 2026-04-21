# This is a multiplication table generator
print("Welcome to the multiplication table generator!")
print("----------------------------------------------")
x = int(input("Please input a number of your choice: "))
for i in range(1, 13):
    print(f"{x} x {i} = {x * i}")