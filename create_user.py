import sqlite3
import hashlib

def create_user(username, password, email):
    conn = sqlite3.connect('iot_dashboard.db')
    cursor = conn.cursor()
    
    # Hash the password (simple MD5 for now - we'll improve this later)
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    
    try:
        cursor.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, hashed_password, email)
        )
        conn.commit()
        print(f"User '{username}' created successfully!")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists!")
    except Exception as e:
        print(f"Error: {e}")
    
    conn.close()

# Create a test user
create_user('admin', 'admin123', 'admin@example.com')
create_user('testuser', 'test123', 'test@example.com')
