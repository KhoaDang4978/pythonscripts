# This is a simple calculator
print('Please input your first number: ')
num1 = int(input())
print('Please input your second number: ')
num2 = int(input())
print('Please choose your operation: +, -, *, /')
operation = str(input())
result = 0

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num2 - num1
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Cannot devide by zero!")
    else:
        result = num1 / num2
else:
    print("Invalid operation!")
print("Result: " + str(result))
