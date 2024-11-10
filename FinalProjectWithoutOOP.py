import json
from datetime import datetime, timedelta

# Load tasks from file
def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    priority = input("Enter priority (High, Medium, Low): ").capitalize().strip()

    # Validate date input
    try:
        datetime.strptime(due_date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")



# View all tasks with optional filtering
def view_tasks(tasks, filter_by=None):
    filtered_tasks = tasks
    if filter_by == "due_date":
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        filtered_tasks = [task for task in tasks if task['due_date'] == due_date]
    elif filter_by == "priority":
        priority = input("Enter priority (High, Medium, Low): ").capitalize().strip()
        filtered_tasks = [task for task in tasks if task['priority'] == priority]
    
    if not filtered_tasks:
        print("No tasks found with the specified filter.")
    else:
        for i, task in enumerate(filtered_tasks, 1):
            print(f"Task {i}: {task['title']} (Due: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']})")

# Update a task
def update_task(tasks):
    title = input("Enter the title of the task to update: ").strip()
    for task in tasks:
        if task['title'].lower() == title.lower():
            task['title'] = input("Enter new task title (press Enter to skip): ").strip() or task['title']
            task['description'] = input("Enter new description (press Enter to skip): ").strip() or task['description']
            new_due_date = input("Enter new due date (YYYY-MM-DD) (press Enter to skip): ").strip()
            if new_due_date:
                try:
                    datetime.strptime(new_due_date, '%Y-%m-%d')
                    task['due_date'] = new_due_date
                except ValueError:
                    print("Invalid date format! Keeping the original due date.")
            task['priority'] = input("Enter new priority (High, Medium, Low) (press Enter to skip): ").capitalize().strip() or task['priority']
            print("Task updated successfully!")
            return
    print("Task not found!")

# Delete a task
def delete_task(tasks):
    title = input("Enter the title of the task to delete: ").strip()
    for task in tasks:
        if task['title'].lower() == title.lower():
            tasks.remove(task)
            print("Task deleted successfully!")
            return
    print("Task not found!")

# Mark a task as completed
def mark_task_completed(tasks):
    title = input("Enter the title of the task to mark as completed: ").strip()
    for task in tasks:
        if task['title'].lower() == title.lower():
            task['completed'] = True
            print("Task marked as completed!")
            return
    print("Task not found!")

# Search for tasks by title or keywords
def search_tasks(tasks):
    keyword = input("Enter keyword or title to search: ").lower().strip()
    found_tasks = [task for task in tasks if keyword in task['title'].lower() or keyword in task['description'].lower()]
    
    if found_tasks:
        for i, task in enumerate(found_tasks, 1):
            print(f"Task {i}: {task['title']} (Due: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']})")
    else:
        print("No tasks found with that keyword!")

# Sort tasks by due date, priority, or completion status
# Sort tasks by due date, priority, or completion status
def sort_tasks(tasks):
    sort_by = input("Sort by (due_date/priority/completed): ").lower()
    
    if sort_by == "due_date":
        # Update the date parsing to match the expected input format
        sorted_tasks = sorted(tasks, key=lambda task: datetime.strptime(task['due_date'], '%d/%m/%Y'))
    elif sort_by == "priority":
        priority_map = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(tasks, key=lambda task: priority_map.get(task['priority'], 4))
    elif sort_by == "completed":
        sorted_tasks = sorted(tasks, key=lambda task: task['completed'])
    else:
        print("Invalid sort option!")
        return

    for i, task in enumerate(sorted_tasks):
        print(f"Task {i+1}: {task['title']} (Due: {task['due_date']}, Priority: {task['priority']}, Completed: {task['completed']})")

# Reminders: Check if any tasks are due today
def task_reminders(tasks):
    today = datetime.today().strftime('%Y-%m-%d')
    due_today = [task for task in tasks if task['due_date'] == today]
    
    if due_today:
        print("Tasks due today:")
        for task in due_today:
            print(f"- {task['title']} (Priority: {task['priority']})")
    else:
        print("No tasks due today.")

# Main function for the task manager system
def main():
    tasks = load_tasks("tasks.json")
    
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
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            filter_option = input("Filter by (due_date/priority/none): ").lower().strip()
            if filter_option == 'due_date':
                view_tasks(tasks, filter_by="due_date")
            elif filter_option == 'priority':
                view_tasks(tasks, filter_by="priority")
            else:
                view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_completed(tasks)
        elif choice == '6':
            search_tasks(tasks)
        elif choice == '7':
            sort_tasks(tasks)
        elif choice == '8':
            task_reminders(tasks)
        elif choice == '9':
            save_tasks("tasks.json", tasks)
            print("Tasks saved and program exited.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
