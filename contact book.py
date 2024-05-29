#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:





# In[ ]:




