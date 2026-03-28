import os

FILE_NAME = "database.txt"

# CREATE Append data
def add_blocker():
    blocker = input("Enter your Daily Blocker: ")

    with open(FILE_NAME, "a") as file:
        file.write(blocker + "\n")

    print("Blocker saved successfully.\n")


# READ Fetch data
def fetch_blockers():
    if not os.path.exists(FILE_NAME):
        print("Warning: The file does not exist yet.\n")
        return

    with open(FILE_NAME, "r") as file:
        blockers = file.readlines()

    if len(blockers) == 0:
        print("No blockers found.\n")
    else:
        print("\n--- Team Daily Blockers ---")
        for i, blocker in enumerate(blockers, start=1):
            print(f"{i}. {blocker.strip()}")
        print()


# WARNING before overwrite
def overwrite_file():
    if os.path.exists(FILE_NAME):
        confirm = input("Warning: This will overwrite all data. Continue? (yes/no): ")
        if confirm.lower() != "yes":
            print("Operation cancelled.\n")
            return

    new_data = input("Enter new content: ")

    with open(FILE_NAME, "w") as file:
        file.write(new_data + "\n")

    print("File overwritten successfully.\n")


# MENU
def menu():
    while True:
        print("=== Team Daily Status System ===")
        print("1. Add Blocker")
        print("2. Fetch Blockers")
        print("3. Overwrite File")
        print("4. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_blocker()
        elif option == "2":
            fetch_blockers()
        elif option == "3":
            overwrite_file()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


# RUN PROGRAM
menu()


"""
--- ENGLISH PRACTICE SECTION ---

Protocol selection (3-C Rule):

1. I will reach out to the team via Slack because the issue is an immediate blocker that needs quick attention.
2. I would use Email if the problem requires a detailed explanation and documentation.
3. I will use Jira to formally report the bug and track its resolution in the system.

Vocabulary integration:

This script uses Persistence to store daily blockers in a text file so the data is not lost after closing the program. 
The Fetch function allows users to retrieve and display all saved information efficiently. 
Additionally, the system includes a warning before any Overwrite action to prevent accidental data loss. 
If an issue occurs, the user can reach out to the team using the appropriate communication channel.
"""