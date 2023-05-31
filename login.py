import sqlite3 #Import sqlite3 library for DB management
import tkinter as tk #Import the tkinter library for GUI
from tkinter import messagebox #Import messagebox to display messages to the user
from database import *

#Defining the user class
class User:
    #Initializer for the User class, sets the user's first name, last name, username, and password.
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    #Static method that checks if the provided username and password exist in the pyflora.db database
    @staticmethod
    def check_user(username, password):
        conn = sqlite3.connect('pyflora.db') #Connect to the pyflora.db database
        cursor = conn.cursor()  #Get a cursor object that can execute SQL commands
        
        #Execute an SQL query to find the user with the provided username and password.
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone() #Fetch the result of the query, returns None if the user is not found
        conn.close() #Close the DB connection
        return result is not None   #Return True if a user was found, False if user is not found.
    

    def login(self):
        username = username_entry.get() #Get the entered username.
        password = password_entry.get() #Get the entered password.

        #Call the check_user method to verify if username and pass are correct.
        #Print success message and redirect to main menu if yes, print error if not.
        if User.check_user(username, password):
            messagebox.showinfo("Success, Login Successful!") 
            # TODO: Redirect to the main menu
        else:
            messagebox.showerror("Error, invalid username or password.")

#Creating a user using the User class        
user1 = User("Teo", "Venus", "tvenus", "sifra")
#Inserting the user in the database
insert_user(user1.first_name, user1.last_name, user1.username, user1.password)

#Creating the main window for the login screen
root = tk.Tk()
root.title("Login") #Set the title of the window
root.geometry("300x200") #Set the size of the window


#Create a label and text entry for the username
username_label = tk.Label(root, text="Username: ")
username_label.grid(row=0, column=0, padx=10, pady=10, sticky="e") #Add it to the window
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

#Create a label and text entry for the password
password_label = tk.Label(root, text="Password: ")
password_label.grid(row=1, column=0, padx=10, pady=10, sticky="e" ) #Add it to the window
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

#Create a login button
login_button = tk.Button(root, text="Login", command=user1.login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()