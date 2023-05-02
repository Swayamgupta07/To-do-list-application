import os

tasks = []

def remove_task():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(tasks):
            tasks.pop(choice - 1)
            print("Task removed successfully!")
        else:
            print("Invalid task number. Please try again.")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    print("Tasks saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
            print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No tasks file found. Starting with an empty task list.")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Save tasks")
    print("5. Load tasks")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        save_tasks()
    elif choice == "5":
        load_tasks()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# cleanup by removing the tasks file if it's empty
if len(tasks) == 0 and os.path.exists("tasks.txt"):
    os.remove("tasks.txt")
