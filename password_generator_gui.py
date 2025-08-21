import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        all_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(all_chars) for _ in range(length))
        password_display.config(text=f"Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a phone number.")

# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("350x200")
window.resizable(False, False)

# Length input
tk.Label(window, text="Enter password length:").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack()

# Generate button
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

# Display result
password_display = tk.Label(window, text="Password: ", font=("Arial", 12))
password_display.pack(pady=10)

# Run the GUI
window.mainloop()
