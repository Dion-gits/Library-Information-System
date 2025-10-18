import mysql.connector

# Add this improved setup function
def setup_database_enhanced():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
        cursor.execute("USE library_db")

        # Enhanced tables with proper relationships
        tables = [
            """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id VARCHAR(50) UNIQUE NOT NULL,
                full_name VARCHAR(100) NOT NULL,
                age INT,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(100),
                contact VARCHAR(20),
                address TEXT,
                status ENUM('Active', 'Not Active') DEFAULT 'Active',
                fees DECIMAL(10,2) DEFAULT 0.00,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                isbn VARCHAR(20) UNIQUE NOT NULL,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(100) NOT NULL,
                publication_year INT,
                quantity INT DEFAULT 1,
                available INT DEFAULT 1,
                genre VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_id INT,
                user_id INT,
                transaction_type ENUM('borrow', 'return') NOT NULL,
                borrow_date DATE,
                due_date DATE,
                return_date DATE,
                status ENUM('active', 'returned', 'overdue') DEFAULT 'active',
                fine DECIMAL(10,2) DEFAULT 0.00,
                days_overdue INT DEFAULT 0,
                book_title VARCHAR(255),
                user_name VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
            """
        ]

        for table in tables:
            cursor.execute(table)

        # Insert sample data with more realistic transactions
        sample_users = [
            ("U001", "John Doe", 25, "password123", "john@email.com", "123-4567", "123 Main St", "Active", 0.00),
            ("U002", "Jane Smith", 30, "password123", "jane@email.com", "987-6543", "456 Oak Ave", "Active", 0.00),
            ("U003", "Bob Wilson", 22, "password123", "bob@email.com", "555-1234", "789 Pine Rd", "Active", 5.00)
        ]

        for user in sample_users:
            cursor.execute(
                "INSERT IGNORE INTO users (user_id, full_name, age, password, email, contact, address, status, fees) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                user
            )

        sample_books = [
            ("978-0134685991", "Effective Java", "Joshua Bloch", 2018, 5, 3, "Programming"),
            ("978-0201633610", "Design Patterns", "Erich Gamma", 1994, 3, 1, "Computer Science"),
            ("978-0061120084", "To Kill a Mockingbird", "Harper Lee", 1960, 2, 2, "Fiction"),
            ("978-0451524935", "1984", "George Orwell", 1949, 4, 4, "Fiction")
        ]

        for book in sample_books:
            cursor.execute(
                "INSERT IGNORE INTO books (isbn, title, author, publication_year, quantity, available, genre) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                book
            )

        # Sample transactions for analytics
        from datetime import datetime, timedelta
        sample_transactions = [
            (1, 1, 'borrow', (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d'),
             (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'), None, 'returned', 0.00, 0),
            (2, 1, 'borrow', (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
             (datetime.now() + timedelta(days=9)).strftime('%Y-%m-%d'), None, 'active', 0.00, 0),
            (3, 2, 'borrow', (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d'),
             (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'), None, 'overdue', 5.00, 1),
            (1, 1, 'return', (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d'),
             (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d'),
             (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'), 'returned', 0.00, 0),
        ]

        for trans in sample_transactions:
            cursor.execute(
                """INSERT IGNORE INTO transactions 
                (book_id, user_id, transaction_type, borrow_date, due_date, return_date, status, fine, days_overdue) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                trans
            )

        conn.commit()
        print("✅ Enhanced database setup completed successfully!")

    except Exception as e:
        print(f"❌ Enhanced database setup failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()


# setup_enhanced.py


if __name__ == "__main__":
    setup_database_enhanced()
    print("🎉 Enhanced database setup complete!")
    print("📊 Your analytics will now show real transaction data.")