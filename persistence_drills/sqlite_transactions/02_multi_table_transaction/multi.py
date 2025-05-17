import sqlite3

def update_multiple_tables():
    try:
        # Connect to the database (or create it)
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY,
                customer_name TEXT,
                status TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_details (
                detail_id INTEGER PRIMARY KEY,
                order_id INTEGER,
                product_name TEXT,
                quantity INTEGER,
                FOREIGN KEY(order_id) REFERENCES orders(order_id)
            )
        ''')

        # Insert sample data if empty
        cursor.execute('SELECT COUNT(*) FROM orders')
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO orders (customer_name, status) VALUES (?, ?)", ("Alice", "Pending"))
            cursor.execute("INSERT INTO order_details (order_id, product_name, quantity) VALUES (?, ?, ?)", (1, "Widget", 10))
            conn.commit()

        # Start transaction
        conn.execute('BEGIN')

        # Update orders table
        cursor.execute("UPDATE orders SET status = ? WHERE order_id = ?", ("Shipped", 1))

        # Update order_details table
        cursor.execute("UPDATE order_details SET quantity = ? WHERE detail_id = ?", (15, 1))

        # Commit the transaction if both updates succeed
        conn.commit()
        print("Transaction committed successfully.")

    except Exception as e:
        # Rollback on any error
        conn.rollback()
        print("Transaction failed and rolled back.")
        print("Error:", e)

    finally:
        conn.close()

if __name__ == "__main__":
    update_multiple_tables()
