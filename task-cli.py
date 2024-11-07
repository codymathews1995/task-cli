import argparse
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

class Task:
    def __init__(self, description, task_list):
        if task_list:
            self.id = max(task['id'] for task in task_list) + 1
        else:
            self.id = len(task_list) + 1
            
        self.description = description
        self.status = "Pending"
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = datetime.now().isoformat()
        
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                tasks = json.load(file)
                return tasks
        except json.JSONDecodeError:
            print("Error reading task file. Starting with an empty task list.")
        
    else:
        print("No existing task file found, starting with an empty list.")
        return []

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
            print(f"Saved tasks to {TASKS_FILE}")
    except Exception as e:
        print(f'Error saving tasks: {e}')
        

def add_task(description):
    tasks = load_tasks()
    new_task = Task(description, tasks)
    tasks.append(new_task.to_dict())
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task.id})")

def remove_task(task_id):
    tasks = load_tasks()
    task_to_remove = None
    
    for task in tasks:
        if task['id'] == task_id:
            task_to_remove = task
            break
    
    if task_to_remove:
        tasks.remove(task_to_remove)
        save_tasks(tasks)
        print(f"Task with ID {task_id} has been removed")
    else:
        print(f"No task found with ID {task_id}")

def list_tasks():
    tasks = load_tasks()  # Reuse load_tasks() to get the tasks

    if not tasks:  # Check if there are no tasks
        print("No tasks found.")
        return
    
    # Print the header for better formatting
    print(f"{'ID':<5} {'Description':<30} {'Status':<15} {'Created At':<20} {'Updated At':<20}")
    print("-" * 90)

    # Print each task's details
    for task in tasks:
        print(f"{task['id']:<5} {task['description'][:30]:<30} {task['status']:<15} {task['createdAt']:<20} {task['updatedAt']:<20}")

def update_status(task_id, new_status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task ID {task_id} status updated to {new_status}.")
            return
    print(f"No task found with ID {task_id}")


def main():
    parser = argparse.ArgumentParser(description="A task manager for the CLI.")
    parser.add_argument("--add", "-a", type=str, help="Add a task with a description.")
    parser.add_argument("--remove", "-r", type=int, help="Remove a task by ID.")
    parser.add_argument("--list", "-l", action="store_true", help="Lists all tasks.")
    parser.add_argument("--update-status", "-u", type=int, nargs=2, metavar=("ID", "STATUS"),
                        help="Update the status of a task by ID and new status.")
    
    args = parser.parse_args()
    
    if args.add:
        add_task(args.add)
    elif args.remove:
        remove_task(args.remove)
    elif args.list:
        list_tasks()
    elif args.update_status:
        task_id = args.update_status[0]
        new_status = args.update_status[1]
        update_status(task_id, new_status)
    else:
        print("Please specify an action. Use --help for more information.")

if __name__ == "__main__":
    main()