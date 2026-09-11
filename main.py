import tkinter as tk
from tkinter import messagebox


# -----------------------------
# Button functions
# -----------------------------

def show_welcome():
    name = name_entry.get().strip()

    if name == "":
        messagebox.showwarning("Missing Name", "Please enter your name.")
        return

    result_label.config(
        text=f"Welcome, {name}! 🚀\nYour hackathon journey starts here!"
    )


def clear_screen():
    name_entry.delete(0, tk.END)
    result_label.config(text="")


# -----------------------------
# Create main window
# -----------------------------

window = tk.Tk()
window.title("AI Hackathon Dashboard")
window.geometry("600x450")
window.configure(bg="#101827")


# -----------------------------
# Title
# -----------------------------

title_label = tk.Label(
    window,
    text="🚀 AI HACKATHON DASHBOARD",
    font=("Arial", 22, "bold"),
    fg="#00e5ff",
    bg="#101827"
)

title_label.pack(pady=30)


# -----------------------------
# Description
# -----------------------------

description_label = tk.Label(
    window,
    text="Your first Python + Tkinter project",
    font=("Arial", 13),
    fg="white",
    bg="#101827"
)

description_label.pack(pady=5)


# -----------------------------
# Name input
# -----------------------------

name_label = tk.Label(
    window,
    text="Enter your name:",
    font=("Arial", 12),
    fg="white",
    bg="#101827"
)

name_label.pack(pady=(30, 5))


name_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=30,
    justify="center"
)

name_entry.pack(pady=5)


# -----------------------------
# Buttons
# -----------------------------

button_frame = tk.Frame(window, bg="#101827")
button_frame.pack(pady=25)


welcome_button = tk.Button(
    button_frame,
    text="START 🚀",
    font=("Arial", 12, "bold"),
    bg="#00c853",
    fg="white",
    width=12,
    command=show_welcome
)

welcome_button.grid(row=0, column=0, padx=10)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 12, "bold"),
    bg="#ff1744",
    fg="white",
    width=12,
    command=clear_screen
)

clear_button.grid(row=0, column=1, padx=10)


# -----------------------------
# Result
# -----------------------------

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold"),
    fg="#ffd740",
    bg="#101827"
)

result_label.pack(pady=20)


# -----------------------------
# Keep application running
# -----------------------------

window.mainloop()
