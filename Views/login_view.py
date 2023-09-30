import tkinter as tk
from tkinter import ttk
from controllers.login_controller import authenticate

#Function to submit login
def submit_login():
    username = username_entry.get()
    password = password_entry.get()
    
    if authenticate(username, password):
        print("Success")
    else:
        print("Login failed. Wrong credentials.")

#Tkinter window initialization
root = tk.Tk()
root.title("PyFlora Login")
root.geometry("600x450")

#Centralizing the window
root.eval('tk::PlaceWindow . center')

#Username label and entry field
username_label = ttk.Label(root, text="Username:")
username_label.pack(pady=5)
username_entry = ttk.Entry(root, width=30)
username_entry.pack(pady=5)

#Password label and entry field
password_label = ttk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = ttk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Login button
login_button = ttk.Button(root, text="Login", command=submit_login)
login_button.pack(pady=20)

root.mainloop()