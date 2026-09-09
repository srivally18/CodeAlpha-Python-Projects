import sqlite3


# Database connection
def connect_db():
    return sqlite3.connect("expenses.db")


# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Add transaction
def add_transaction(date, description, category, amount, transaction_type):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (date, description, category, amount, transaction_type)
        VALUES (?, ?, ?, ?, ?)
    """, (date, description, category, amount, transaction_type))

    conn.commit()
    conn.close()


# Get all transactions
def get_transactions():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data


# Delete transaction
def delete_transaction(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,)
    )

    conn.commit()
    conn.close()
