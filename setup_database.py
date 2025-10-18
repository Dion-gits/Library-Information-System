import mysql.connector

def setup_database():
    try:
        # Connect without specifying database first
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        cursor = conn.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
        cursor.execute("USE library_db")

        # Create tables
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
                book_title VARCHAR(255),
                user_name VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]

        for table in tables:
            cursor.execute(table)

        # Insert sample data
        sample_users = [
            ("U001", "John Doe", 25, "password123", "john@email.com", "123-4567", "123 Main St", "Active", 0.00),
            ("U002", "Jane Smith", 30, "password123", "jane@email.com", "987-6543", "456 Oak Ave", "Active", 0.00)
        ]

        for user in sample_users:
            cursor.execute(
                "INSERT IGNORE INTO users (user_id, full_name, age, password, email, contact, address, status, fees) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                user
            )

        sample_books = [
            ("978-0134685991", "Effective Java", "Joshua Bloch", 2018, 5, "Programming"),
            ("978-0201633610", "Design Patterns", "Erich Gamma", 1994, 3, "Computer Science")
        ]

        for book in sample_books:
            cursor.execute(
                "INSERT IGNORE INTO books (isbn, title, author, publication_year, quantity, genre) VALUES (%s, %s, %s, %s, %s, %s)",
                book
            )

        conn.commit()
        print("✅ Database setup completed successfully!")

    except Exception as e:
        print(f"❌ Database setup failed: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    setup_database()