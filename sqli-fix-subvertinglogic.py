
import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="123456",  # Replace with your MySQL password
    database="sql_injection_demo"  # Replace with the name of your database
)
cursor = conn.cursor()

# Create the table and insert data
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(50)
);
''')

# cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("admin", "123", "admin"))
# cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("Lam", "lamthd2705", "user"))
# cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", ("Thanh", "thanhht1902", "user"))
# conn.commit()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))  # Pass inputs as parameters
    user = cursor.fetchone()
    if user:
        # Successful login
        return f"Login successful. Welcome, {user[1]}!"
    else:
        # Failed login
        return f"Login failed. Invalid username or password."

result = login()
print(result)

cursor.close()
conn.close()