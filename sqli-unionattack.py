
import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="123456",  # Replace with your MySQL password
    database="sql_injection_demo"  # Replace with the name of your database
)
cursor = conn.cursor()

def getProduct():
    name = input("Enter product name: ")
    # ' UNION SELECT username, password FROM users --   
    query = f"SELECT name, description FROM products WHERE name = '{name}'"
    cursor.execute(query)
    products = cursor.fetchall()
    # If a result is found, print the name and description
    if products:
        for product in products:
        # Unpack each row (name and description) in the products table
            if len(product) == 2:
                name, description = product
                print(f"Name: {name}, Description: {description}")
            else:
                print("Unexpected data returned: ", product)
    else:
        # If no product is found, print this message
        print("Invalid name.")

getProduct()

cursor.close()
conn.close()