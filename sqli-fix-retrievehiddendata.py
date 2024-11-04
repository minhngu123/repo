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
    price INT
);
''')

# cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Widget", 25))
# cursor.execute("INSERT INTO products (name, price) VALUES (%s, %s)", ("Gizmo", 50))
# conn.commit()

# Fix using parameterized queries (prepared statements)
def get_product_secure(user_input):
    query = "SELECT * FROM products WHERE price = %s"
    cursor.execute(query, (user_input,))
    return cursor.fetchall()

user_input = input("Enter price: ")
products = get_product_secure(user_input)
print(products)

# Close the connection
cursor.close()
conn.close()
