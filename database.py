import sqlite3
import os

# Create SQLite database file
DB_PATH = 'iot_dashboard.db'

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

# Create a callable database class
class DatabaseConnection:
    def __init__(self):
        self.conn = None
        print("[success] SQLite database connection created!")
    
    def __call__(self, username, host, password, database_name):
        # Ignore the MySQL parameters, just return self for SQLite
        return self
    
    def cursor(self):
        if not self.conn:
            self.conn = get_db_connection()
        return self.conn.cursor()
    
    def commit(self):
        if self.conn:
            self.conn.commit()
    
    def execute(self, query, params=None):
        cursor = self.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor
    
    def close(self):
        if self.conn:
            self.conn.close()

# Create the expected db object
db = DatabaseConnection()

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create tables based on the SQL script you have
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT,
            last_login TIMESTAMP,
            api_key TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_name TEXT,
            device_id TEXT UNIQUE,
            username TEXT,
            status TEXT,
            last_seen TIMESTAMP
        )
    ''')
    
    # Add more tables as needed based on your SQL file
    conn.commit()
    conn.close()
    print("[success] SQLite database initialized!")

# Initialize the database
init_db()
