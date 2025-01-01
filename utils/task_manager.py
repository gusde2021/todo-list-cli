```python
import os
from utils.file_handler import FileHandler

class TaskManager:
    def __init__(self):
        self.file_handler = FileHandler("tasks.json")
        self.tasks = self.file_handler.load_tasks()

    def add_task(self, description, deadline):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "deadline": deadline,
            "completed": False
        }
        self.tasks.append(task)
        self.file_handler.save_tasks(self.tasks)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                status = "Completed" if task["completed"] else "Pending"
                print(f"ID: {task['id']} | Task: {task['description']} | Deadline: {task['deadline']} | Status: {status}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.file_handler.save_tasks(self.tasks)
                print("Task marked as completed!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.file_handler.save_tasks(self.tasks)
        print("Task deleted successfully!")
```
