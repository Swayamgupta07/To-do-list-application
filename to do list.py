tasks = []
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        print("Tasks:")
        for task in tasks:
            print("- " + task)
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")