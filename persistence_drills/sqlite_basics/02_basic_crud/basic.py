import sqlite3

DB_NAME = "store.db"

def connect_db():
    """Connect to SQLite DB (creates if not exists) and return the connection."""
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    """Create the products table if it doesn't exist."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_product(name, price):
    """Insert a new product into the products table."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
    conn.commit()
    conn.close()

def fetch_all_products():
    """Fetch and print all records from the products table."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Price: {row[2]}")

def update_product_price(product_id, new_price):
    """Update the price of a product based on its id."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    """Delete a product from the table by its id."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()

    # Example usage:
    insert_product("Apple", 0.5)
    insert_product("Banana", 0.3)

    print("All products:")
    fetch_all_products()

    print("\nUpdating price of product ID 1 to 0.6")
    update_product_price(1, 0.6)

    print("\nAll products after update:")
    fetch_all_products()

    print("\nDeleting product ID 2")
    delete_product(2)

    print("\nAll products after deletion:")
    fetch_all_products()
