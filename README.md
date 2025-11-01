# 📝 To-Do List CLI App

A simple command-line To-Do List application written in Python. This project allows users to manage tasks with features like adding, viewing, editing, deleting, searching, filtering, and marking tasks as completed. Tasks are saved to a local file for persistence.

---

## 🚀 Features

- Add tasks with priority and due date
- View all tasks with status, priority, and due date
- Delete tasks
- Mark tasks as completed
- Edit task titles
- Search tasks by keyword (title, priority, or due date)
- Filter tasks by:
  - Completion status
  - Priority level
  - Due date
- Persistent storage using JSON file (`task_file.txt`)

---

## 📦 Requirements

- Python 3.x

No external libraries are required.

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/gotanmay/to_do_python.git
   cd to_do_python

Run the script:

python todo.py

Follow the on-screen menu to manage your tasks.

📂 File Structure

to_do_python/

├── todo.py          # Main script with all functionality

├── task_file.txt    # Auto-generated file to store tasks

📌 Notes

Changes are only saved when you exit the program using the menu option.

If task_file.txt doesn't exist, it will be created automatically.

📄 License

This project is open-source under the MIT License.
