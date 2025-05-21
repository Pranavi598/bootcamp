import sqlite3

def transfer_funds(from_account_id, to_account_id, amount):
    try:
        conn = sqlite3.connect('store.db')
        cursor = conn.cursor()

        # Create accounts table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                account_id INTEGER PRIMARY KEY,
                balance REAL NOT NULL
            )
        ''')

        # Insert dummy accounts if none exist (for demo)
        cursor.execute("SELECT COUNT(*) FROM accounts")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO accounts (account_id, balance) VALUES (?, ?)", (1, 1000))
            cursor.execute("INSERT INTO accounts (account_id, balance) VALUES (?, ?)", (2, 500))
            conn.commit()

        # Start transaction
        conn.execute('BEGIN')

        # Check balances
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (from_account_id,))
        from_balance = cursor.fetchone()
        if from_balance is None:
            raise ValueError(f"From account {from_account_id} does not exist")
        if from_balance[0] < amount:
            raise ValueError("Insufficient funds")

        # Debit from_account
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, from_account_id))

        # Credit to_account
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, to_account_id))

        # Commit transaction
        conn.commit()
        print(f"Transferred {amount} from account {from_account_id} to {to_account_id} successfully.")

    except Exception as e:
        conn.rollback()
        print("Transaction failed and rolled back.")
        print("Error:", e)

    finally:
        conn.close()


if __name__ == "__main__":
    transfer_funds(1, 2, 200)
