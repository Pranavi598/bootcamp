import sqlite3
from datetime import datetime

def update_inventory(product_id, quantity_change):
    """
    Updates product inventory count and logs the change atomically.
    quantity_change can be positive or negative.
    """
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Create tables if not exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                inventory_count INTEGER DEFAULT 0
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory_log (
                log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                change INTEGER,
                timestamp TEXT,
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        ''')

        # Insert dummy product if not exists (for demo)
        cursor.execute("SELECT COUNT(*) FROM products WHERE id = ?", (product_id,))
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO products (id, name, inventory_count) VALUES (?, ?, ?)", (product_id, "Demo Product", 100))
            conn.commit()

        # Start transaction
        conn.execute('BEGIN')

        # Update inventory count
        cursor.execute("SELECT inventory_count FROM products WHERE id = ?", (product_id,))
        current_count = cursor.fetchone()
        if current_count is None:
            raise ValueError(f"Product with id {product_id} not found")
        new_count = current_count[0] + quantity_change
        if new_count < 0:
            raise ValueError("Inventory cannot be negative")

        cursor.execute("UPDATE products SET inventory_count = ? WHERE id = ?", (new_count, product_id))

        # Log the inventory change
        timestamp = datetime.now().isoformat()
        cursor.execute("INSERT INTO inventory_log (product_id, change, timestamp) VALUES (?, ?, ?)",
                       (product_id, quantity_change, timestamp))

        # Commit transaction
        conn.commit()
        print(f"Inventory updated to {new_count} and change logged successfully.")

    except Exception as e:
        conn.rollback()
        print("Transaction failed and rolled back.")
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    # Example: subtract 20 from inventory
    update_inventory(1, -20)
