import json
from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, priority, completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority.capitalize()
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return [Task(**task_data) for task_data in json.load(file)]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file)

    def is_valid_date(self, date_str):
        """ Check if the given date string is a valid date in 'YYYY-MM-DD' format. """
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError: 
            return False

    def add_task(self, title, description, due_date, priority):
        if not self.is_valid_date(due_date):
            print("Invalid due date format! Please use YYYY-MM-DD.")
            return
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self, filter_by=None):
        filtered_tasks = self.tasks
        if filter_by == "due_date":
            due_date = input("Enter due date (YYYY-MM-DD): ")
            filtered_tasks = [task for task in self.tasks if task.due_date == due_date]
        elif filter_by == "priority":
            priority = input("Enter priority (High, Medium, Low): ").capitalize()
            filtered_tasks = [task for task in self.tasks if task.priority == priority]

        for i, task in enumerate(filtered_tasks):
            print(f"Task {i+1}: {task.title} (Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed})")

    def update_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.title = input("Enter new task title: ") or task.title
                task.description = input("Enter new description: ") or task.description
                
                while True:
                    new_due_date = input("Enter new due date (YYYY-MM-DD): ") or task.due_date
                    if self.is_valid_date(new_due_date):
                        task.due_date = new_due_date
                        break
                    else:
                        print("Invalid due date format! Please use YYYY-MM-DD.")
                
                task.priority = input("Enter new priority (High, Medium, Low): ").capitalize() or task.priority
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task deleted successfully!")
                return
        print("Task not found!")

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                print("Task marked as completed!")
                return
        print("Task not found!")

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        if found_tasks:
            for i, task in enumerate(found_tasks):
                print(f"Task {i+1}: {task.title} (Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed})")
        else:
            print("No tasks found with that keyword!")

    def sort_tasks(self, sort_by):
        if sort_by == "due_date":
            self.tasks.sort(key=lambda task: datetime.strptime(task.due_date, '%Y-%m-%d'))
        elif sort_by == "priority":
            priority_map = {"High": 1, "Medium": 2, "Low": 3}
            self.tasks.sort(key=lambda task: priority_map.get(task.priority, 4))
        elif sort_by == "completed":
            self.tasks.sort(key=lambda task: task.completed)

        for i, task in enumerate(self.tasks):
            print(f"Task {i+1}: {task.title} (Due: {task.due_date}, Priority: {task.priority}, Completed: {task.completed})")

    def task_reminders(self):
        today = datetime.today().strftime('%Y-%m-%d')
        due_today = [task for task in self.tasks if task.due_date == today]
        
        if due_today:
            print("Tasks due today:")
            for task in due_today:
                print(f"- {task.title} (Priority: {task.priority})")
        else:
            print("No tasks due today.")

def main():
    task_manager = TaskManager("tasks.json")
    
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Search Task")
        print("7. Sort Tasks")
        print("8. Task Reminders")
        print("9. Save & Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (High, Medium, Low): ").capitalize()
            task_manager.add_task(title, description, due_date, priority)
        elif choice == '2':
            filter_option = input("Filter by (due_date/priority/none): ").lower()
            if filter_option == 'due_date':
                task_manager.view_tasks(filter_by="due_date")
            elif filter_option == 'priority':
                task_manager.view_tasks(filter_by="priority")
            else:
                task_manager.view_tasks()
        elif choice == '3':
            title = input("Enter the title of the task to update: ")
            task_manager.update_task(title)
        elif choice == '4':
            title = input("Enter the title of the task to delete: ")
            task_manager.delete_task(title)
        elif choice == '5':
            title = input("Enter the title of the task to mark as completed: ")
            task_manager.mark_task_completed(title)
        elif choice == '6':
            keyword = input("Enter keyword or title to search: ").lower()
            task_manager.search_tasks(keyword)
        elif choice == '7':
            sort_by = input("Sort by (due_date/priority/completed): ").lower()
            task_manager.sort_tasks(sort_by)
        elif choice == '8':
            task_manager.task_reminders()
        elif choice == '9':
            task_manager.save_tasks()
            print("Tasks saved and program exited.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
