from datetime import datetime
import argparse
import sys
import json

class Task:
    """
    Represents a task with id, description, status, and timestamps.
    """

    def __init__(self, id, description, status="todo"):
        """
        Initializes a Task object.
        """
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = datetime.now().isoformat()

    def update(self, description=None, status=None):
        """
        Updates the task's description and/or status.
        """
        if description:
            self.description = description
        if status:
            self.status = status
        self.updatedAt = datetime.now().isoformat()

    def to_dict(self):
        """
        Returns the task as a dictionary.
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

def load_tasks():
    """
    Loads tasks from the tasks.json file.
    """
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"Error loading tasks: {e}")
        return []

def save_tasks(tasks):
    """
    Saves tasks to the tasks.json file.
    """
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def create_task(id, description):
    """
    Creates a new task and saves it to the tasks.json file.
    """
    try:
        tasks = load_tasks()
        task = Task(id, description)
        tasks.append(task.to_dict())
        save_tasks(tasks)
    except Exception as e:
        print(f"Error creating task: {e}")

def update_task(args):
    """
    Updates an existing task and saves it to the tasks.json file.
    """
    try:
        tasks = load_tasks()
        for task in tasks:
            if task['id'] == args.id:
                task['description'] = args.description
                task['status'] = args.status
                save_tasks(tasks)
                return
        print("Task not found")
    except Exception as e:
        print(f"Error updating task: {e}")

def delete_task(args):
    """
    Deletes a task from the tasks.json file.
    """
    try:
        tasks = load_tasks()
        tasks = [task for task in tasks if task['id'] != args.id]
        save_tasks(tasks)
    except Exception as e:
        print(f"Error deleting task: {e}")

def list_tasks(args):
    """
    Lists all tasks.
    """
    tasks = load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

def list_done_tasks(args):
    """
    Lists all done tasks.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'done':
            print(f"ID: {task['id']}, Description: {task['description']}")

def list_not_done_tasks(args):
    """
    Lists all not done tasks.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['status'] != 'done':
            print(f"ID: {task['id']}, Description: {task['description']}")

def list_in_progress_tasks(args):
    """
    Lists all in progress tasks.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['status'] == 'in-progress':
            print(f"ID: {task['id']}, Description: {task['description']}")

def mark_in_progress(args):
    """
    Marks a task as in progress.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == args.id:
            task['status'] = 'in-progress'
            save_tasks(tasks)
            return
    print("Task not found")

def mark_done(args):
    """
    Marks a task as done.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == args.id:
            task['status'] = 'done'
            save_tasks(tasks)
            return
    print("Task not found")

def main():
    """
    Main entry point for the Task Tracker CLI.
    """
    parser = argparse.ArgumentParser(description='Task Tracker')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('id', type=int, help='Unique identifier for the task')
        add_parser.add_argument('description', type=str, help='Task description')
    add_parser.set_defaults(func=lambda args: create_task(args.id, args.description))

    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument('description', type=str, help='Task description')
    update_parser.add_argument('status', type=str, help='Task status')
    update_parser.set_defaults(func=lambda args: update_task(args))

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')
    delete_parser.set_defaults(func=lambda args: delete_task(args))

    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.set_defaults(func=list_tasks)

    list_done_parser = subparsers.add_parser('list_done', help='List all done tasks')
    list_done_parser.set_defaults(func=list_done_tasks)

    list_not_done_parser = subparsers.add_parser('list_not_done', help='List all not done tasks')
    list_not_done_parser.set_defaults(func=list_not_done_tasks)

    list_in_progress_parser = subparsers.add_parser('list_in_progress', help='List all in progress tasks')
    list_in_progress_parser.set_defaults(func=list_in_progress_tasks)

    in_progress_parser = subparsers.add_parser('in_progress', help='Mark a task as in progress')
    in_progress_parser.add_argument('id', type=int, help='Task ID')
    in_progress_parser.set_defaults(func=lambda args: mark_in_progress(args))

    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('id', type=int, help='Task ID')
    done_parser.set_defaults(func=lambda args: mark_done(args))

    args = parser.parse_args()
    if args.command:
        try:
            args.func(args)
        except Exception as e:
            print(f"Error executing command: {e}")
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
