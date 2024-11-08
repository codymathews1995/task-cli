# task-cli

A simple command-line tool to manage tasks. Based on the projects from roadmap.sh.

[https://roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

## Features

- Add, remove, list, and update tasks with status management.
- JSON-based storage.

## Usage

```python
# Add a task
python task_manager.py --add "Task description"
```

```python
# Remove a task by ID
python task_manager.py --remove <ID>
```

```python
# List all tasks
python task_manager.py --list
```

```python
# Update task status by ID
python task_manager.py --update-status <ID> <STATUS>
```

## Dependencies

- Python
- argparse, json, datetime, os
