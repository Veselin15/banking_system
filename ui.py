import tkinter as tk
from tkinter import messagebox
from account_operations import login, create_account, is_valid_password, get_balance

def on_login(username_entry, password_entry, window, username_label, password_label, login_button, register_button):
    username = username_entry.get()
    password = password_entry.get()
    if login(username, password):
        # Hide login fields and buttons
        username_label.pack_forget()
        password_label.pack_forget()
        username_entry.pack_forget()
        password_entry.pack_forget()
        login_button.pack_forget()
        register_button.pack_forget()

        # Show the balance in the same window
        show_balance(window, username)
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

def show_balance(window, username):
    # Get the balance of the user
    balance = get_balance(username)

    # Display the balance
    balance_label = tk.Label(window, text=f"Your balance: ${balance}")
    balance_label.pack()

    # Optionally, add a logout button or other options
    logout_button = tk.Button(window, text="Logout", command=window.quit)
    logout_button.pack()

def create_login_screen():
    window = tk.Tk()
    window.title("Banking System")
    window.geometry("400x300")
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
    login_button = tk.Button(window, text="Login", command=lambda: on_login(username_entry, password_entry, window, username_label, password_label, login_button, register_button))
    login_button.pack()

    register_button = tk.Button(window, text="Register", command=lambda: on_register(username_entry, password_entry))
    register_button.pack()

    window.mainloop()
