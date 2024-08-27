import unittest
import json
import os
from task_tracker import (
    load_tasks,
    save_tasks,
    create_task,
    update_task,
    delete_task,
    list_tasks,
    list_done_tasks,
    list_not_done_tasks,
    list_in_progress_tasks,
    mark_in_progress,
    mark_done
)

class TestTaskTracker(unittest.TestCase):
    """
    Test cases for Task Tracker functionality.
    """

    def setUp(self):
        """
        Set up test data before each test case.
        """
        self.tasks = [
            {"id": 1, "description": "Task 1", "status": "todo", "createdAt": "2024-01-01T00:00:00", "updatedAt": "2024-01-01T00:00:00"},
            {"id": 2, "description": "Task 2", "status": "in-progress", "createdAt": "2024-01-02T00:00:00", "updatedAt": "2024-01-02T00:00:00"},
            {"id": 3, "description": "Task 3", "status": "done", "createdAt": "2024-01-03T00:00:00", "updatedAt": "2024-01-03T00:00:00"}
        ]
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def test_load_tasks(self):
        """
        Test loading tasks from JSON file.
        """
        tasks = load_tasks()
        self.assertEqual(tasks, self.tasks)

    def test_save_tasks(self):
        """
        Test saving tasks to JSON file.
        """
        new_task = {"id": 4, "description": "Task 4", "status": "todo", "createdAt": "2024-01-04T00:00:00", "updatedAt": "2024-01-04T00:00:00"}
        self.tasks.append(new_task)
        save_tasks(self.tasks)
        tasks = load_tasks()
        self.assertEqual(tasks, self.tasks)

    def test_create_task(self):
        """
        Test creating a new task.
        """
        create_task(5, "Task 5")
        tasks = load_tasks()
        self.assertEqual(len(tasks), 4)

    def test_update_task(self):
        """
        Test updating an existing task.
        """
        args = self._create_args(2, "Task 2 updated", "done")
        update_task(args)
        tasks = load_tasks()
        self.assertEqual(tasks[1]["description"], "Task 2 updated")
        self.assertEqual(tasks[1]["status"], "done")

    def test_delete_task(self):
        """
        Test deleting a task.
        """
        args = self._create_args(1)
        delete_task(args)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 2)

    def test_list_tasks(self):
        """
        Test listing all tasks.
        """
        args = self._create_args()
        list_tasks(args)

    def test_list_done_tasks(self):
        """
        Test listing done tasks.
        """
        args = self._create_args()
        list_done_tasks(args)

    def test_list_not_done_tasks(self):
        """
        Test listing not done tasks.
        """
        args = self._create_args()
        list_not_done_tasks(args)

    def test_list_in_progress_tasks(self):
        """
        Test listing in progress tasks.
        """
        args = self._create_args()
        list_in_progress_tasks(args)

    def test_mark_in_progress(self):
        """
        Test marking a task as in progress.
        """
        args = self._create_args(1)
        mark_in_progress(args)
        tasks = load_tasks()
        self.assertEqual(tasks[0]["status"], "in-progress")

    def test_mark_done(self):
        """
        Test marking a task as done.
        """
        args = self._create_args(1)
        mark_done(args)
        tasks = load_tasks()
        self.assertEqual(tasks[0]["status"], "done")

    def tearDown(self):
        """
        Clean up test data after each test case.
        """
        os.remove('tasks.json')

    def _create_args(self, *args):
        """
        Helper method to create Args object.
        """
        class Args:
            def __init__(self, *args):
                self.id = args[0] if args else None
                self.description = args[1] if len(args) > 1 else None
                self.status = args[2] if len(args) > 2 else None
        return Args(*args)

if __name__ == '__main__':
    unittest.main()