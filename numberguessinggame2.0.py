# This is a number guessing game with a limit of 7 attempts
print("Welcome to the guessing game! Good luck!")
print("----------------------------------------")
import random
i = random.randint(1, 100)
count = 7
while True:
    guess = int(input("Guess a number: "))
    if guess == i:
        print("Correct!")
        break
    else: 
        print("Aw!")
        count -= 1
        print(f"You have {count} attempts left!")
        if guess > i:
            print("Too high, go lower!")
        elif guess < 67:
            print("Too low, go higher!")
    if count == 0:
            print(f"Game over! The answer was {i}!")
            break