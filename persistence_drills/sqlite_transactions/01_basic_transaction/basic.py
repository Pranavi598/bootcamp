import sqlite3

def basic_transaction():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()

    # Create customers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()

    try:
        conn.execute('BEGIN')  # Start transaction

        # Insert multiple customers
        cursor.execute('INSERT INTO customers (name, email) VALUES (?, ?)', ('Alice', 'alice@example.com'))
        cursor.execute('INSERT INTO customers (name, email) VALUES (?, ?)', ('Bob', 'bob@example.com'))

        # Commit transaction
        conn.commit()
        print("Transaction committed successfully.")
    except Exception as e:
        conn.rollback()
        print("Transaction failed, rollback done.", e)
    finally:
        conn.close()

if __name__ == "__main__":
    basic_transaction()
