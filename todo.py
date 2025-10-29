import json
def load_task():
    """Called at start to load the task file"""
    global tasks
    try:
        with open("task_file.txt", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print("No previous task file found, new file will be created upon save.")
        tasks = []

def save_task():
    """Called after adding or deleting a task"""
    with open("task_file.txt", "w") as file:
        json.dump(tasks, file, indent=4)

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
    print("5. Mark Task as Completed")
    print("6. Edit Task")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        priority = input("Priority (Enter 1 > 2 > 3): ")
        due = input("Enter due date (YYYY-MM-DD): ")
        tasks.append({"title": task, "completed": False, "priority": priority, "due": due })
        print("Task added!")
        unsaved_changes = True

    elif choice == '2':
        if not tasks:
            print("There is no task, you are all set.")
        else:
            print('Your tasks:')
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Not completed"
                print(f"{i}. {task['title']} [{status}] [Priority: {task['priority']}] [Due: {task['due']}]")

    elif choice == '3':
        delete_task_num = int(input("Enter the number of the task to delete: "))
        if 0 < delete_task_num <= len(tasks):
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

    elif choice == '5':
        task_to_mark = int(input("Enter the number of the task to mark as complete: "))
        if 0 < task_to_mark <= len(tasks):
            tasks[task_to_mark - 1]["completed"] = True
            print("Marked completed:", tasks[task_to_mark - 1]['title'])
            unsaved_changes = True
        else:
            print("Invalid task number or to-do is empty!")

    elif choice == '6':
        task_to_edit = int(input("Enter the number of the task to edit: "))
        if 0 < task_to_edit <= len(tasks):
            new_title = input("Enter the new title: ")
            tasks[task_to_edit - 1]["title"] = new_title
            print("Edited task:", tasks[task_to_edit - 1]['title'])
            unsaved_changes = True
        else:
            print("Invalid task number or to-do is empty!")

    else:
        print("Invalid choice entered.")
