class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the to-do list."""
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def remove_task(self, task_index):
        """Remove a task from the to-do list."""
        try:
            task_index = int(task_index)
            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                print(f"Task '{removed_task}' removed successfully.")
            else:
                print("Error: Invalid task index.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid task index.")

    def display_tasks(self):
        """Display all tasks in the to-do list."""
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")
        else:
            print("To-Do List is empty.")


def main():
    print("Welcome to the To-Do List Manager")

    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task_index = input("Enter the task index to remove: ")
            todo_list.remove_task(task_index)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Thank you for using the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
