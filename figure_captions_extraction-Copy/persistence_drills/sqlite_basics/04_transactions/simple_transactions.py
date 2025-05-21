import sqlite3

class Product:
    DB_NAME = "store.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_NAME)
        self.create_table()

    def create_table(self):
        """Create products table if it doesn't exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_product(self, name, price):
        """Add a new product."""
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', (name, price))
        self.conn.commit()

    def update_product_price(self, product_id, new_price):
        """Update price of a product by id."""
        cursor = self.conn.cursor()
        cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        """Delete product by id."""
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
        self.conn.commit()

    def list_products(self):
        """Fetch and return all products."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM products')
        return cursor.fetchall()

    def close(self):
        """Close the DB connection."""
        self.conn.close()


if __name__ == "__main__":
    # Example usage
    p = Product()

    # Add products
    p.add_product("Apple", 0.5)
    p.add_product("Banana", 0.3)

    # List products
    print("Products:")
    for prod in p.list_products():
        print(f"ID: {prod[0]}, Name: {prod[1]}, Price: {prod[2]}")

    # Update product price
    p.update_product_price(1, 0.6)

    print("\nAfter price update:")
    for prod in p.list_products():
        print(f"ID: {prod[0]}, Name: {prod[1]}, Price: {prod[2]}")

    # Delete a product
    p.delete_product(2)

    print("\nAfter deletion:")
    for prod in p.list_products():
        print(f"ID: {prod[0]}, Name: {prod[1]}, Price: {prod[2]}")

    p.close()
