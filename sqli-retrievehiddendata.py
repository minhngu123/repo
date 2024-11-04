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
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    description VARCHAR(50),
    price INT
);
''')

cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s)", ("iPhone", "smartphone", 25))
cursor.execute("INSERT INTO products (name, description, price) VALUES (%s, %s, %s)", ("Asus", "laptop", 50))
conn.commit()

# Vulnerable function that fetches product based on user input
def get_product(user_input):
    query = f"SELECT * FROM products WHERE price = {user_input}"
    cursor.execute(query)
    return cursor.fetchall()

# Attacker input could be: '25 OR 1=1'
user_input = input("Enter price: ")
products = get_product(user_input)
print(products)

# Close the connection
cursor.close()
conn.close()
