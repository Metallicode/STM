class Task:
    def __init__(self, name, due_date, priority):
        pass


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        pass

    def delete_task(self, task_name):
        pass

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.name}, Due: {task.due_date}, Priority: {task.priority}, State: {task.state}")

    # Add methods for other task manipulations: mark as done, sort view, etc.

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nSimple Task Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("q Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Task name: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            new_task = Task(name, due_date, priority)
            task_manager.add_task(new_task)
            print(f"Task '{name}' added successfully!")

        elif choice == "2":
            name = input("Enter the task name to delete: ")
            if task_manager.delete_task(name):
                print(f"Task '{name}' deleted successfully!")
            else:
                print("Task not found!")

        elif choice == "3":
            print("\nTasks:")
            task_manager.view_tasks()

        elif choice == "q":
            print("Exiting. Have a great day!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
