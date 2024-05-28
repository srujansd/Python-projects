#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Rock-Paper-Scissors Game
import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()


# In[3]:


# Contact Book
import sys

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        if not results:
            print("No matching contacts found.")
        else:
            for contact in results:
                print(contact)

    def update_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print("Contact found:")
                print(contact)
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contact.name = name
                contact.phone = phone
                contact.email = email
                contact.address = address
                print("Contact updated successfully.")
                return
        print("No matching contact found to update.")

    def delete_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("No matching contact found to delete.")

    def user_interface(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == '4':
                query = input("Enter name or phone number to update: ")
                self.update_contact(query)
            elif choice == '5':
                query = input("Enter name or phone number to delete: ")
                self.delete_contact(query)
            elif choice == '6':
                print("Exiting the Contact Manager. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.user_interface()


# In[4]:


# Task-3 Password generator
import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    password = generate_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()


# In[5]:


# CALCULATOR
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator")
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            
            print(f"The result is: {result}")
            break
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

if __name__ == "__main__":
    main()


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




