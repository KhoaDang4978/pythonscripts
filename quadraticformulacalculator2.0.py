# This is a quadratic func calculator
print("Welcome to the quadratic function calculator")
print("--------------------------------------------")
print("Please follow this format: Ax^2 + Bx + C (A,B,C > 0)")
print("Please input first value: ax^2")
a = float(input())
print("Please input second value: bx")
b = float(input())
print("Please input third value: c")
c = float(input())
import cmath
d = (b**2 - 4*a*c)
sqrt_d = cmath.sqrt(d)
x1 = (-b + sqrt_d) / 2*a
print("X1: " + str(x1))
x2 = (-b - sqrt_d) /2*a
print("X2: " + str(x2))