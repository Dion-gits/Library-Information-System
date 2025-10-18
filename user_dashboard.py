from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class UserDashboardWindow:
    def setupUi(self, MainWindow, user_data):
        MainWindow.setObjectName("UserDashboardWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.user_data = user_data
        self.db = Database()

        # Top frame
        self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(-10, -40, 821, 101))
        self.top_frame.setStyleSheet("background-color: #E0B3FF;")
        self.top_frame.setObjectName("top_frame")

        # Logo
        self.logo = QtWidgets.QLabel(parent=self.top_frame)
        self.logo.setGeometry(QtCore.QRect(0, 20, 111, 111))
        self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")
        self.logo.setObjectName("logo")

        # Name label
        self.label = QtWidgets.QLabel(parent=self.top_frame)
        self.label.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label.setScaledContents(True)
        self.label.setStyleSheet("background: transparent;")
        self.label.setObjectName("label")

        # Title
        self.label_title = QtWidgets.QLabel("USER DASHBOARD", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(350, 60, 201, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("color: white;")
        self.label_title.setObjectName("label_title")

        # Main frame
        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.main_frame.setStyleSheet("background-color: #e2d8f3;")
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")

        # User info section
        self.user_info_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.user_info_frame.setGeometry(QtCore.QRect(50, 30, 671, 200))
        self.user_info_frame.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            border: 2px solid #7C3AED;
        """)
        self.user_info_frame.setObjectName("user_info_frame")

        # Currently borrowed books section
        self.borrowed_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.borrowed_frame.setGeometry(QtCore.QRect(50, 250, 671, 250))
        self.borrowed_frame.setStyleSheet("""
            background-color: white;
            border-radius: 10px;
            border: 2px solid #7C3AED;
        """)
        self.borrowed_frame.setObjectName("borrowed_frame")

        self.borrowed_label = QtWidgets.QLabel("Currently Borrowed Books", parent=self.borrowed_frame)
        self.borrowed_label.setGeometry(QtCore.QRect(20, 10, 631, 30))
        self.borrowed_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #7C3AED;")
        self.borrowed_label.setObjectName("borrowed_label")

        self.borrowed_list = QtWidgets.QListWidget(parent=self.borrowed_frame)
        self.borrowed_list.setGeometry(QtCore.QRect(20, 50, 631, 180))
        self.borrowed_list.setStyleSheet("background-color: #f8fafc; border: 1px solid #e2e8f0;")
        self.borrowed_list.setObjectName("borrowed_list")

        # Logout button
        self.logout_btn = QtWidgets.QPushButton("LOGOUT", parent=self.main_frame)
        self.logout_btn.setGeometry(QtCore.QRect(650, 520, 100, 35))
        self.logout_btn.setStyleSheet("background-color: #DC2626; color: white; font-weight: bold;")
        self.logout_btn.setObjectName("logout_btn")
        self.logout_btn.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)

        # Load user details and borrowed books
        self.load_user_details()
        self.load_borrowed_books()

    def load_user_details(self):
        """Load user details including fees and status"""
        try:
            # First get the user's database ID
            user_id_query = "SELECT id FROM users WHERE user_id = %s"
            user_id_result = self.db.fetch_one(user_id_query, (self.user_data['user_id'],))

            if not user_id_result:
                print(f"User not found: {self.user_data['user_id']}")
                return

            user_db_id = user_id_result['id']

            # Now get user details
            query = "SELECT full_name, email, status, fees FROM users WHERE id = %s"
            user = self.db.fetch_one(query, (user_db_id,))

            if user:
                # Welcome message
                welcome_label = QtWidgets.QLabel(f"Welcome, {user['full_name']}!", parent=self.user_info_frame)
                welcome_label.setGeometry(QtCore.QRect(20, 20, 631, 30))
                welcome_label.setStyleSheet("font-size: 20px; font-weight: bold; color: #7C3AED;")
                welcome_label.setObjectName("welcome_label")

                # User info
                info_label = QtWidgets.QLabel(
                    f"User ID: {self.user_data['user_id']} | Email: {user['email']}",
                    parent=self.user_info_frame
                )
                info_label.setGeometry(QtCore.QRect(20, 60, 631, 25))
                info_label.setStyleSheet("font-size: 14px; color: #4b5563;")
                info_label.setObjectName("info_label")

                # Status and fees
                status_color = "#dc2626" if user['status'] == 'Not Active' else "#059669"
                status_label = QtWidgets.QLabel(
                    f"Status: {user['status']} | Outstanding Fees: ₱{float(user['fees']):.2f}",
                    parent=self.user_info_frame
                )
                status_label.setGeometry(QtCore.QRect(20, 90, 631, 25))
                status_label.setStyleSheet(f"font-size: 14px; font-weight: bold; color: {status_color};")
                status_label.setObjectName("status_label")

                # Warning message if account is deactivated
                if user['status'] == 'Not Active':
                    warning_label = QtWidgets.QLabel(
                        "⚠️ Your account has been deactivated due to overdue books!\n"
                        "Please contact the librarian to settle your fees and reactivate your account.",
                        parent=self.user_info_frame
                    )
                    warning_label.setGeometry(QtCore.QRect(20, 120, 631, 60))
                    warning_label.setStyleSheet("""
                        background-color: #fef2f2;
                        color: #dc2626;
                        font-size: 12px;
                        border: 1px solid #fca5a5;
                        border-radius: 5px;
                        padding: 8px;
                    """)
                    warning_label.setWordWrap(True)
                    warning_label.setObjectName("warning_label")
                elif float(user['fees']) > 0:
                    warning_label = QtWidgets.QLabel(
                        f"⚠️ You have outstanding fees of ₱{float(user['fees']):.2f}\n"
                        "Please settle your fees to avoid account deactivation.",
                        parent=self.user_info_frame
                    )
                    warning_label.setGeometry(QtCore.QRect(20, 120, 631, 50))
                    warning_label.setStyleSheet("""
                        background-color: #fffbeb;
                        color: #d97706;
                        font-size: 12px;
                        border: 1px solid #fcd34d;
                        border-radius: 5px;
                        padding: 8px;
                    """)
                    warning_label.setWordWrap(True)
                    warning_label.setObjectName("warning_label")

        except Exception as e:
            print(f"Error loading user details: {e}")

    def load_borrowed_books(self):
        """Load currently borrowed books for the user"""
        try:
            # First get the user's database ID
            user_id_query = "SELECT id FROM users WHERE user_id = %s"
            user_id_result = self.db.fetch_one(user_id_query, (self.user_data['user_id'],))

            if not user_id_result:
                print(f"User not found for borrowed books: {self.user_data['user_id']}")
                self.borrowed_list.addItem("Error: User not found")
                return

            user_db_id = user_id_result['id']

            # Query for borrowed books using the database ID
            query = """
                SELECT b.title, t.borrow_date, t.due_date 
                FROM transactions t
                JOIN books b ON t.book_id = b.id
                WHERE t.user_id = %s AND t.transaction_type = 'borrow' AND t.status = 'active'
                ORDER BY t.due_date ASC
            """
            borrowed_books = self.db.fetch_all(query, (user_db_id,))

            self.borrowed_list.clear()
            if borrowed_books:
                for book in borrowed_books:
                    # Calculate days remaining/overdue
                    from datetime import datetime
                    due_date = datetime.strptime(str(book['due_date']), '%Y-%m-%d')
                    today = datetime.now()
                    days_diff = (due_date - today).days

                    if days_diff < 0:
                        status_text = f"OVERDUE ({abs(days_diff)} days)"
                        item_text = f"{book['title']} (Due: {book['due_date']}) - {status_text}"
                    elif days_diff <= 3:
                        status_text = f"DUE SOON ({days_diff} days)"
                        item_text = f"{book['title']} (Due: {book['due_date']}) - {status_text}"
                    else:
                        item_text = f"{book['title']} (Due: {book['due_date']}) - {days_diff} days remaining"

                    self.borrowed_list.addItem(item_text)
            else:
                self.borrowed_list.addItem("No currently borrowed books")

        except Exception as e:
            print(f"Error loading borrowed books: {e}")
            self.borrowed_list.clear()
            self.borrowed_list.addItem("Error loading borrowed books")