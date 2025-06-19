tasks = []

def display_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{i}. {task['title']}  |  Status: {status}")

def add_task():
    title = input("Enter task title: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    print("Task added successfully.")

def update_task():
    display_tasks()
    try:
        index = int(input("Enter the task number to update: "))
        if 1 <= index <= len(tasks):
            new_title = input("Enter new title: ")
            tasks[index - 1]["title"] = new_title
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    display_tasks()
    try:
        index = int(input("Enter the task number to mark as completed: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    display_tasks()
    try:
        index = int(input("Enter the task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Task '{removed['title']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n====== To-Do List Menu ======")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid input. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()