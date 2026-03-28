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



"""
--- ENGLISH PRACTICE SECTION ---

Protocol selection (3-C Rule):

1. I would reach out to the team via Slack because it is the fastest way to communicate an urgent issue.
2. I would use Email if I need to explain the problem in more detail and keep a formal record.
3. I would use Jira to report the issue properly and make sure it is tracked until it gets solved.


Vocabulary integration:

This script uses persistence to save the daily blockers in a file, so the information is not lost after closing the program. 
The fetch feature allows the user to read all the saved data in a simple way. 
Also, before doing an overwrite, the program shows a warning to avoid losing important information. 
If something goes wrong, I can reach out to the team using the right communication channel.
"""

