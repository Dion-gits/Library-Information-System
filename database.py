import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "library_db"

    def connect(self):
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as e:
            print(f"❌ Database Connection Error: {e}")
            return None

    def execute_query(self, query, params=None):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params or ())
                connection.commit()
                return True
            except Error as e:
                print(f"❌ Query Error: {e}")
                return False
            finally:
                cursor.close()
                connection.close()
        return False

    def fetch_one(self, query, params=None):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute(query, params or ())
                return cursor.fetchone()
            except Error as e:
                print(f"❌ Fetch One Error: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
        return None

    def fetch_all(self, query, params=None):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query, params or ())
            results = cursor.fetchall()
            cursor.close()
            conn.close()
            return results
        except Exception as e:
            print(f"❌ Fetch All Error: {e}")
            return []