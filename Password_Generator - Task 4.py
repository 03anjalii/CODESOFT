# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import string
import secrets
import tkinter as tk
from tkinter import messagebox

def generate_password():
    alphabets = string.ascii_letters
    numbers = string.digits
    special_char = string.punctuation

    password = alphabets + numbers + special_char

    pass_length = int(password_length.get())

    while True:
        pwd = ''.join(secrets.choice(password) for _ in range(pass_length))
        if any(char in special_char for char in pwd) and sum(char in numbers for char in pwd)>= 3:
            break

    generated_password.set(pwd)

def accept_password():
    messagebox.showinfo("Accepted", "Password accepted!")

def reject_password():
    messagebox.showinfo("Rejected", "Password rejected!")

# Create the main window
window = tk.Tk()
window.geometry("700x500")   #size of the window is mentioned here
window.title("Password Generator")
window.configure(background="black")

# Username label and entry
username_label = tk.Label(window, text="Username  :", font=('arial', 10, 'bold'))
username_label.pack(pady=10)
username_entry = tk.Entry(window,fg="black", bg="white")
username_entry.pack(pady=4)

# Password length label and entry
password_length_label = tk.Label(window, text="Password Length :", font=('Arial', 10, "bold"))
password_length_label.pack(pady=2)
password_length = tk.Entry(window, fg="black", bg="white")
password_length.pack(pady=4)

# Generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password, fg="black", bg="grey")
generate_button.pack(pady=5)


# Generated password label
generated_password = tk.StringVar()
generated_password_label = tk.Label(window, textvariable=generated_password, font=('Arial', 10, "bold"))
generated_password_label.pack(pady=2)

# Buttons for accepting or rejecting the password
accept_button = tk.Button(window, text="Accept", command=accept_password)
accept_button.pack( pady=3)
reject_button = tk.Button(window, text="Reject", command=reject_password)
reject_button.pack(pady=3)

# Start the GUI event loop
window.mainloop()


