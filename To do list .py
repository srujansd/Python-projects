#!/usr/bin/env python
# coding: utf-8

# In[1]:


# TASK-1 To-Do-List
import sys

class ToDoItem:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.description}"

class ToDoList:
    def __init__(self):
        self.items = []

    def add_item(self, description):
        new_item = ToDoItem(description)
        self.items.append(new_item)
        print("Task added successfully.")

    def update_item(self, index, new_description):
        if 0 <= index < len(self.items):
            self.items[index].description = new_description
            print("Task updated successfully.")
        else:
            print("Invalid index. Please try again.")

    def mark_complete(self, index):
        if 0 <= index < len(self.items):
            self.items[index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid index. Please try again.")

    def delete_item(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index. Please try again.")

    def display_items(self):
        if not self.items:
            print("No tasks found.")
        else:
            for idx, item in enumerate(self.items, start=1):
                print(f"{idx}. {item}")

def main():
    todo_list = ToDoList()
    print("Welcome to the To-Do List Manager")

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_item(description)
        elif choice == '2':
            try:
                index = int(input("Enter the task number to update: ")) - 1
                new_description = input("Enter the new task description: ")
                todo_list.update_item(index, new_description)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                index = int(input("Enter the task number to mark as completed: ")) - 1
                todo_list.mark_complete(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                todo_list.delete_item(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            todo_list.display_items()
        elif choice == '6':
            print("Exiting the To-Do List Manager. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




