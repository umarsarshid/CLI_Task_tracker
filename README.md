# Task Tracker CLI
A simple command-line interface for managing tasks.

## Installation
To install, simply clone this repository and run:

```bash
    python main.py
```

## Usage

### Adding a Task

To add a new task, use the following command:

```bash
python main.py add <id> <description>
```

Replace <id> with a unique identifier for the task, and <description> with a brief description of the task.
Example:

```bash
python main.py add 1 "Buy milk"
```

### Updating a Task
To update an existing task, use the following command:

```bash
python main.py update <id> <description> <status>
```

Replace <id> with the ID of the task to update, <description> with the new description, and <status> with the new status (either "todo", "in-progress", or "done").

Example:

```bash
python main.py update 1 "Buy milk and eggs" "in-progress"
```

### Deleting a Task

To delete a task, use the following command:

```bash
python main.py delete <id>
```

Replace <id> with the ID of the task to delete.

Example:

```bash
python main.py delete 1
```
### Listing Tasks
To list all tasks, use the following command:

```bash
python main.py list
```
To list tasks by status, use the following commands:

```bash
python main.py list_done
python main.py list_not_done
python main.py list_in_progress
```

### Marking a Task as In Progress or Done
To mark a task as in progress, use the following command:

```bash
python main.py in_progress <id>
```

To mark a task as done, use the following command:

```bash
python main.py done <id>
```

Replace <id> with the ID of the task to update.
Examples:

```bash
python main.py in_progress 1
python main.py done 1
```
I hope this helps! Let me know if you have any questions or need further assistance.