def load_task():
    """Called at start to load the task file"""
    try:
        with open("task_file.txt", "r") as file:
            content = file.readlines()
            for line in content:
                tasks.append(line.strip())
    except FileNotFoundError:
        print("Tasks file not found, new file will be created upon save.")

def save_task():
    """Called after adding or deleting a task"""
    with open("task_file.txt", "w") as file:
        for item in tasks:
            file.write(item + "\n")

tasks = []
unsaved_changes = False

load_task()

print("="*20)
print("Changes will only be saved if the program is exited from the menu.")
print("="*20)

def show_menu():
    print("\n----To-Do List----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append({"title": task, "completed": False })
        print("Task added!")
        unsaved_changes = True

    elif choice == '2':
        if not tasks:
            print("There is no task, you are all set.")
        else:
            print('Your tasks:')
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Not completed"
                print(f"{i}. {task["title"]} [{status}]")

    elif choice == '3':
        delete_task_num = int(input("Enter the number of the task to delete: "))
        if 0 < delete_task_num < len(tasks):
            print("Deleted task:", tasks.pop(delete_task_num - 1))
            unsaved_changes = True

        else:
            print("Invalid task number or to-do is empty!")

    elif choice == '4':
        print("Exiting.")
        if unsaved_changes:
            save_task()
            print("Changes saved.")
        else:
            print("No changes to save.")
        print("Thanks of using to-do.")
        break

    else:
        print("Invalid choice entered.")
