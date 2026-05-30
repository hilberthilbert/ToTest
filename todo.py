import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ 任务已添加")

def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✘"
        print(f"{i}. [{status}] {t['task']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法：python todo.py [add/list]")
    elif sys.argv[1] == "add":
        add_task(sys.argv[2])
    elif sys.argv[1] == "list":
        list_tasks()