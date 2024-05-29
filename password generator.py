#!/usr/bin/env python
# coding: utf-8

# In[3]:


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


# In[ ]:





# In[ ]:




