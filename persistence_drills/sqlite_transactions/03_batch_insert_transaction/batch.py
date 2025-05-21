import sqlite3

def batch_insert_products(products):
    """
    products: List of tuples [(name, price), ...]
    """
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Create products table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        # Start transaction
        conn.execute('BEGIN')

        # Insert all products
        for name, price in products:
            cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))

        # Commit transaction
        conn.commit()
        print("Batch insert successful.")

    except Exception as e:
        conn.rollback()
        print("Batch insert failed, transaction rolled back.")
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    sample_products = [
        ("Apple", 0.99),
        ("Banana", 0.59),
        ("Orange", 1.29),
    ]
    batch_insert_products(sample_products)
