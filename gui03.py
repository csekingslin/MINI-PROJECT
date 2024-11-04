import tkinter as tk
from tkinter import ttk
import subprocess

def switch_toggle():
    switch_var.set(not switch_var.get())
    if switch_var.get():
        status_label.config(text="CUSTOM MONITORING MODE ON")
    else:
        status_label.config(text="CUSTOM MONITORING MODE OFF")

def virus_button_click():
    subprocess.run(['python', 'virus_scan.py'])

def shield_button_click():
    subprocess.run(['python', 'shield_protection.py'])

def show_about_page():
    # Create a new top-level window for the About page
    about_window = tk.Toplevel(root)
    about_window.title("About Virus Shield")
    about_window.geometry("300x200")

    # Add labels for About information
    about_label = ttk.Label(about_window, text="Virus Shield", font=("Arial", 14))
    about_label.pack(pady=10)

    members_label = ttk.Label(about_window, text="Developed by:", font=("Arial", 12))
    members_label.pack(pady=5)

    member_list = ttk.Label(about_window, text="* Kingslin\n* Sathish Kumar\n* Nantha Kumar\n* Samzer Kumar", font=("Arial", 12))
    member_list.pack(pady=5)

    # Optionally, you can add a close button
    # close_button = ttk.Button(about_window, text="Close", command=about_window.destroy)
    # close_button.pack(pady=10)

root = tk.Tk()
root.title("Virus Shield")
root.geometry("400x300")

style = ttk.Style()
style.theme_use('default')  # Use default theme

title_label = ttk.Label(root, text="VIRUS SHIELD", font=("Arial", 16))
title_label.pack(pady=10)

switch_var = tk.BooleanVar(value=True)
switch_button = ttk.Checkbutton(root, text="", variable=switch_var, command=switch_toggle)
switch_button.pack()

status_label = ttk.Label(root, text="CUSTOM MONITORING MODE ON", font=("Arial", 12))
status_label.pack(pady=10)

virus_button = ttk.Button(root, text="VIRUS", command=virus_button_click)
virus_button.pack(pady=10)

shield_button = ttk.Button(root, text="SHIELD", command=shield_button_click)
shield_button.pack(pady=10)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Add an About menu item
help_menu.add_command(label="About", command=show_about_page)

root.mainloop()
