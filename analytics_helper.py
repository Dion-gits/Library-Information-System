# analytics_helper.py
from database import Database

class AnalyticsHelper:
    @staticmethod
    def get_borrowed_books_count():
        """Get count of currently borrowed books"""
        query = """
            SELECT COUNT(*) as count FROM transactions 
            WHERE status = 'active' AND transaction_type = 'borrow'
        """
        result = Database().fetch_one(query)
        return result['count'] if result else 0

    @staticmethod
    def get_overdue_books_count():
        """Get count of overdue books"""
        query = """
            SELECT COUNT(*) as count FROM transactions 
            WHERE status = 'active' 
            AND transaction_type = 'borrow' 
            AND due_date < CURDATE()
        """
        result = Database().fetch_one(query)
        return result['count'] if result else 0

    @staticmethod
    def get_total_books_count():
        """Get total books count"""
        query = "SELECT COUNT(*) as count FROM books"
        result = Database().fetch_one(query)
        return result['count'] if result else 0

    @staticmethod
    def get_active_users_count():
        """Get active users count"""
        query = "SELECT COUNT(*) as count FROM users WHERE status = 'Active'"
        result = Database().fetch_one(query)
        return result['count'] if result else 0

    @staticmethod
    def get_recent_transactions(limit=5):
        """Get recent transactions for dashboard"""
        query = """
            SELECT t.id, b.title, u.full_name, t.transaction_type, 
                   t.borrow_date, t.due_date, t.return_date, t.status
            FROM transactions t
            JOIN books b ON t.book_id = b.id
            JOIN users u ON t.user_id = u.id
            ORDER BY t.created_at DESC 
            LIMIT %s
        """
        return Database().fetch_all(query, (limit,))