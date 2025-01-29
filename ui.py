import tkinter as tk
from tkinter import messagebox
from account_operations import login, create_account, is_valid_password

def on_login(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if login(username, password):
        messagebox.showinfo("Login Success", "Welcome to the banking system!")
        # Proceed to the main menu (you can create another window for this)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def on_register(username_entry, password_entry):
    username = username_entry.get()
    password = password_entry.get()
    if not is_valid_password(password):
        messagebox.showinfo("Password Requirements", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
    else:
        create_account(username, password)
        messagebox.showinfo("Registration Success", "Account created successfully.")

def create_login_screen():
    window = tk.Tk()
    window.title("Banking System")

    # Username and password input fields
    username_label = tk.Label(window, text="Username")
    username_label.pack()
    username_entry = tk.Entry(window)
    username_entry.pack()

    password_label = tk.Label(window, text="Password")
    password_label.pack()
    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    # Login and Register buttons
    login_button = tk.Button(window, text="Login", command=lambda: on_login(username_entry, password_entry))
    login_button.pack()

    register_button = tk.Button(window, text="Register", command=lambda: on_register(username_entry, password_entry))
    register_button.pack()

    window.mainloop()
