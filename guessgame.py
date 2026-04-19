# This is a simple guessing game
print("Welcome to the guessing game! Good luck!")
print("-------------------------------------------")
i = 67
while True:
    guess = int(input("Guess a number: "))
    if guess == i:
        print("Correct!")
        break
    else: 
        print("Aw!")
        if guess > 67:
            print("Your guess is higher!")
        elif guess < 67:
            print("Your guess is lower!")