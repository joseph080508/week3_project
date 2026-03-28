import os 

FILE_NAME = "database.txt"

# CREATE Append data
def add_blocker():
    blocker = input("Enter your Daily Blocker: ")

    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print("Blocker saved successfully.\n")
