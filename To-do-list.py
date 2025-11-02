import json
import os
FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_name):
    tasks = load_tasks()
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: '{task_name}'")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found!")
        return
    print("\n📝 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        print(f"{i}. {task['task']} - {status}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"🎯 Task '{tasks[index]['task']}' marked as done.")
    else:
        print("⚠️ Invalid task number!")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: '{removed['task']}'")
    else:
        print("⚠️ Task not found!")
def main():
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task_name = input("Enter task: ").strip()
            add_task(task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                index = int(input("Enter task number to mark done: ")) - 1
                mark_done(index)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "4":
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("⚠️ Please enter a valid number!")
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
