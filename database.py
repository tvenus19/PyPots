import sqlite3


#Function to connect to the database.
def connect_db():
    return sqlite3.connect('pyflora.db')


#Function to create the users table where the users that can log in are kept.
def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    """)
    conn.commit()
    conn.close()


#Function to create the plants table in the database.
def create_plants_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        watering_frequency INTEGER NOT NULL
    );

    """)

    conn.commit()
    conn.close()


#Function to create the pypots table in the database.
def create_pypots_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pypots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        plant_id INTEGER,
        sensor_id INTEGER,
        FOREIGN KEY (plant_id) REFERENCES plants (id),
        FOREIGN KEY (sensor_id) REFERENCES sensors (id)
    );
    """)

    conn.commit()
    conn.close()


#Function to create the sensors table in the database.
def create_sensors_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        reading REAL NOT NULL
    );
    """)

    conn.commit()
    conn.close()


#Function to insert the user in the database.
def insert_user(first_name, last_name, username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users (first_name, last_name, username, password)
    VALUES (?, ?, ?, ?)    
   """, (first_name, last_name, username, password))
    conn.commit()
    conn.close()
    
#This calls the table creation functions upon importing the database module
create_users_table()
create_plants_table()
create_pypots_table()
create_sensors_table()