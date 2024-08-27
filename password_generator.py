import string
import secrets
import tkinter as tk
from tkinter import messagebox

# Function to generate a password
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = (
        (string.ascii_uppercase if use_upper else "") +
        (string.ascii_lowercase if use_lower else "") +
        (string.digits if use_digits else "") +
        (string.punctuation if use_special else "")
    )
    
    if not characters:
        raise ValueError("Please select at least one character type.")
    
    return ''.join(secrets.choice(characters) for _ in range(length))

# Function for GUI button click
def generate_password_clicked():
    try:
        length = int(length_entry.get())
        password = generate_password(
            length, 
            uppercase_var.get(), 
            lowercase_var.get(), 
            numbers_var.get(), 
            special_var.get()
        )
        result_label.config(text=f"Password: {password}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
def run_gui():
    root = tk.Tk()
    root.title("Password Generator")

    tk.Label(root, text="Password Length:").pack()
    global length_entry
    length_entry = tk.Entry(root)
    length_entry.pack()

    global uppercase_var, lowercase_var, numbers_var, special_var
    uppercase_var = tk.BooleanVar(value=True)
    lowercase_var = tk.BooleanVar(value=True)
    numbers_var = tk.BooleanVar(value=True)
    special_var = tk.BooleanVar(value=True)

    tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var).pack()
    tk.Checkbutton(root, text="Include Lowercase", variable=lowercase_var).pack()
    tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
    tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

    tk.Button(root, text="Generate Password", command=generate_password_clicked).pack()
    global result_label
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()

# Entry point
if __name__ == "__main__":
    if input("Choose mode: (1) CLI, (2) GUI: ") == '1':
        length = int(input("Enter password length: "))
        password = generate_password(
            length, 
            input("Include uppercase? (y/n): ").lower() == 'y', 
            input("Include lowercase? (y/n): ").lower() == 'y', 
            input("Include numbers? (y/n): ").lower() == 'y', 
            input("Include special characters? (y/n): ").lower() == 'y'
        )
        print(f"Generated Password: {password}")
    else:
        run_gui()
