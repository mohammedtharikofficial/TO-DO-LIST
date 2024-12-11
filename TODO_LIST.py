# Simple To-Do List Program

tasks = []

def display_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} [{status}]")

def add_task():
    name = input("Enter task name: ")
    tasks.append({"name": name, "completed": False})
    print("Task added successfully!")

def mark_completed():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

while True:
    display_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")