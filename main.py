```python
from utils.task_manager import TaskManager

def main():
    print("Welcome to the To-Do List CLI Application!")
    manager = TaskManager()
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task description: ")
            deadline = input("Enter deadline (YYYY-MM-DD): ")
            manager.add_task(task, deadline)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as complete: "))
            manager.complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
