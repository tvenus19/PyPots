import sqlite3 #Import sqlite3 library for DB management
import tkinter as tk #Import the tkinter library for GUI
from tkinter import messagebox

class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    @staticmethod
    def check_user(username, password):
        conn = sqlite3.connect('pyflora.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        conn.close()
        return result is not None

