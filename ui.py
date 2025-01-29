import tkinter as tk
from tkinter import messagebox
from account_operations import login, create_account, is_valid_password, get_balance, deposit, withdraw

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
        account_window(window, username)
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


def account_window(window, username):
    # Create the balance label before referencing it
    balance_label = tk.Label(window, text="Your balance: $0")
    balance_label.pack()

    # Function to update balance display
    def update_balance_label():
        balance = get_balance(username)  # Get the current balance from DB
        balance_label.config(text=f"Your balance: ${balance}")

    # Initial balance display
    update_balance_label()

    # Withdraw popup
    def open_withdraw_popup():
        popup = tk.Toplevel(window)  # Create a new popup window
        popup.title("Withdraw Amount")

        withdraw_label = tk.Label(popup, text="Enter amount to withdraw:")
        withdraw_label.pack()
        withdraw_entry = tk.Entry(popup)
        withdraw_entry.pack()

        def handle_withdraw():
            try:
                amount = float(withdraw_entry.get())
                if amount <= 0:
                    messagebox.showerror("Invalid Amount", "Amount must be greater than zero.")
                    return
                new_balance = withdraw(username, amount)  # Withdraw from the account
                messagebox.showinfo("Withdrawal Success", f"Successfully withdrew ${amount}. New balance: ${new_balance}")
                update_balance_label()  # Update the main window's balance label
                popup.destroy()  # Close the popup window
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number for the withdrawal.")

        withdraw_button = tk.Button(popup, text="Withdraw", command=handle_withdraw)
        withdraw_button.pack()

    # Deposit popup
    def open_deposit_popup():
        popup = tk.Toplevel(window)  # Create a new popup window
        popup.title("Deposit Amount")

        deposit_label = tk.Label(popup, text="Enter amount to deposit:")
        deposit_label.pack()
        deposit_entry = tk.Entry(popup)
        deposit_entry.pack()

        def handle_deposit():
            try:
                amount = float(deposit_entry.get())
                if amount <= 0:
                    messagebox.showerror("Invalid Amount", "Amount must be greater than zero.")
                    return
                new_balance = deposit(username, amount)  # Deposit to the account
                messagebox.showinfo("Deposit Success", f"Successfully deposited ${amount}. New balance: ${new_balance}")
                update_balance_label()  # Update the main window's balance label
                popup.destroy()  # Close the popup window
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number for the deposit.")

        deposit_button = tk.Button(popup, text="Deposit", command=handle_deposit)
        deposit_button.pack()

    # Main window widgets
    withdraw_button = tk.Button(window, text="Withdraw", command=open_withdraw_popup)
    withdraw_button.pack()

    deposit_button = tk.Button(window, text="Deposit", command=open_deposit_popup)
    deposit_button.pack()

    # Logout button
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
