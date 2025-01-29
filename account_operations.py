import bcrypt
from db_connection import connect_db
import re
def is_valid_password(password):
    if len(password) < 8:  # Minimum length check
        return False
    if not re.search(r"[A-Z]", password):  # Check for at least one uppercase letter
        return False
    if not re.search(r"[0-9]", password):  # Check for at least one number
        return False
    return True

def create_account(username, password):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        print(f"Hashed password: {hashed_password}")  # Debug print
        cursor.execute("INSERT INTO accounts (username, password) VALUES (%s, %s)", (username, hashed_password))
        conn.commit()
        cursor.close()
        conn.close()


def login(username, password):
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM accounts WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result:
            # Ensure the hashed password is in bytes (if it's a memoryview object)
            stored_hashed_password = result[0]
            if isinstance(stored_hashed_password, memoryview):
                stored_hashed_password = stored_hashed_password.tobytes()

            # Compare the entered password with the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
                print("Login successful!")
                return True
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

        cursor.close()
        conn.close()

    return False

# account_operations.py
def get_balance(username):
    # You should replace this with actual logic to retrieve the balance.
    # This is a simple placeholder.
    # e.g., fetch balance from a database or in-memory storage.
    user_balance = 1000  # This is a mock value
    return user_balance


