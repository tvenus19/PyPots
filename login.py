import sqlite3
from tkinter import *


class User:
    def __init__(self, ime, prezime, korisnicko_ime, lozinka):
        self.ime = ime
        self.prezime = prezime
        self.korisnicko_ime = korisnicko_ime
        self.lozinka = lozinka

    def provjeri_username(self, username):
        conn = sqlite3.connect("pyflora.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE korisnicko_ime = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def provjeri_lozinku(self, username, lozinka):
        conn = sqlite3.connect("pyflora.db")
        cursor = conn.cursor()
        cursor.execute("SELECT lozinka FROM users WHERE korisnicko_ime = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result is not None and result[0] == lozinka


def stvori_bazu():
    conn = sqlite3.connect("pyflora.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ime TEXT,
            prezime TEXT,
            korisnicko_ime TEXT UNIQUE,
            lozinka TEXT
        )
    """)

    conn.commit()
    conn.close()


def dodaj_korisnika(user):
    if not user.provjeri_username(user.korisnicko_ime):
        conn = sqlite3.connect("pyflora.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (ime, prezime, korisnicko_ime, lozinka) VALUES (?, ?, ?, ?)
        """, (user.ime, user.prezime, user.korisnicko_ime, user.lozinka))

        conn.commit()
        conn.close()


def prijava():
    username = entry_username.get()
    password = entry_password.get()
    if user.provjeri_lozinku(username, password):
        print("Uspješna prijava!")
    else:
        print("Neispravno korisničko ime ili lozinka")


if __name__ == "__main__":
    stvori_bazu()

    ime = "Ivan"
    prezime = "Ivić"
    korisnicko_ime = "ivan.ivic"
    lozinka = "tajna_lozinka"

    user = User(ime, prezime, korisnicko_ime, lozinka)
    dodaj_korisnika(user)

    root = Tk()
    root.title("Prijava")

    Label(root, text="Korisničko ime:").grid(row=0, column=0, sticky=W)
    entry_username = Entry(root)
    entry_username.grid(row=0, column=1)

    Label(root, text="Lozinka:").grid(row=1, column=0, sticky=W)
    entry_password = Entry(root, show="*")
    entry_password.grid(row=1, column=1)

    Button(root, text="Prijavi se", command=prijava).grid(row=2, column=0, columnspan=2)

    root.mainloop()
