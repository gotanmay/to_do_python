tasks = []
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
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if not tasks:
            print("There is no task, you are all set.")
        else:
            print('Your tasks:')
            for i, task in enumerate(tasks, start=1):
                print(f"{i}: {task}")

    elif choice == '3':
        delete_task_num = int(input("Enter the number of the task to delete: "))
        if 0 < delete_task_num < len(tasks):
            print("Deleted task:", tasks.pop(delete_task_num - 1))

        else:
            print("Invalid task number or to-do is empty!")

    elif choice == '4':
        print("Exiting.")
        print("Thanks of using to-do.")
        break

    else:
        print("Invalid choice entered.")