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

