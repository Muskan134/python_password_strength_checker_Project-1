

import re
import tkinter as tk
from tkinter import ttk

# Function to check password strength
def check_password_strength(password):
    score = 0
    
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'[0-9]', password):
        score += 1
    if re.search(r'[!@#$%^&*()._+-=?/]', password):
        score += 1

    return score
    

# Update UI based on password strength
def update_strength():
    password = entry.get()
    score = check_password_strength(password)

    if score == 0:
        strength_label.config(text="")
        progress['value'] = 0

    elif score <= 2:
        strength_label.config(text="Weak Password", fg="red")
        progress['value'] = 40

    elif score == 3 or score == 4:
        strength_label.config(text="Medium Password", fg="orange")
        progress['value'] = 70

    elif score == 5:
        strength_label.config(text="Strong Password", fg="green")
        progress['value'] = 100


# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.config(bg="#1e1e2f")

# Title
title = tk.Label(root, text="Password Strength Checker",
                 font=("Helvetica", 16, "bold"),
                 bg="#1e1e2f", fg="white")
title.pack(pady=20)

# Password Entry
entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
entry.pack(pady=10)
entry.bind("<KeyRelease>", lambda event: update_strength())

# Strength Label
strength_label = tk.Label(root, text="",
                          font=("Arial", 12, "bold"),
                          bg="#1e1e2f")
strength_label.pack(pady=5)

# Progress Bar
progress = ttk.Progressbar(root, length=250, mode='determinate')
progress.pack(pady=10)

# Run App
root.mainloop()
