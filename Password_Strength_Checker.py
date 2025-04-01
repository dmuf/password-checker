import hashlib
import requests
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in password):
        strength += 1

    if strength == 4:
        return "Strong 💪"
    elif strength == 3:
        return "Medium 🟡"
    else:
        return "Weak ❌"

def check_pwned_api(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first5, rest = sha1_password[:5], sha1_password[5:]

    response = requests.get(f"https://api.pwnedpasswords.com/range/{first5}")
    if rest in response.text:
        return "⚠️ This password has been found in data breaches!"
    return "✅ This password is safe."

def evaluate_password():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password!")
        return
    
    strength_result = check_password_strength(password)
    breach_result = check_pwned_api(password)

    result_label.config(text=f"Strength: {strength_result}\n{breach_result}")

def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        toggle_btn.config(text="Hide Password")
    else:
        password_entry.config(show='*')
        toggle_btn.config(text="Show Password")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

tk.Label(root, text="Enter your password:").pack(pady=5)

password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

toggle_btn = tk.Button(root, text="Show Password", command=toggle_password)
toggle_btn.pack(pady=5)

check_btn = tk.Button(root, text="Check Password", command=evaluate_password)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300)
result_label.pack(pady=10)

root.mainloop()
