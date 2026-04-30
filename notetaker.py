# This is a note taker
import os
while True:
    if os.path.exists("note.txt"):
        with open("note.txt") as f:
            print(f.read())
        with open("note.txt", "a") as f:
            note = input("Note (or exit to quit): ")
            if note == "exit":
                break
            f.write(note + "\n")
    else: 
        f = open("note.txt", "x")
        f.close()
        with open("note.txt", "a") as f:
            f.write(input("Note: ") + "\n")