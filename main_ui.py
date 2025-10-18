from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class Main_ui:
    def setupUi(self, main_base):
        main_base.setObjectName("main_base")
        main_base.resize(766, 637)
        main_base.setMinimumSize(QtCore.QSize(766, 637))
        main_base.setMaximumSize(QtCore.QSize(766, 637))
        main_base.setStyleSheet("background-color: #ffffff;")

        self.centralwidget = QtWidgets.QWidget(parent=main_base)
        self.centralwidget.setObjectName("centralwidget")


        self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(-10, -40, 821, 101))
        self.top_frame.setStyleSheet("background-color: #E0B3FF;")


        self.logo = QtWidgets.QLabel(parent=self.top_frame)
        self.logo.setGeometry(QtCore.QRect(0, 20, 111, 111))
        self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet("background: transparent;")


        self.label_name = QtWidgets.QLabel(parent=self.top_frame)
        self.label_name.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label_name.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label_name.setScaledContents(True)
        self.label_name.setStyleSheet("background: transparent;")


        self.label_title = QtWidgets.QLabel("ADMIN DASHBOARD", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(380, 60, 251, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("color: white;")


        self.logout_btn = QtWidgets.QPushButton("LOGOUT", parent=self.top_frame)
        self.logout_btn.setGeometry(QtCore.QRect(670, 60, 81, 25))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)
        self.logout_btn.setFont(font_btn)
        self.logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #EF4444; 
                color: white; 
                border-radius: 5px;
                border: 2px solid #DC2626;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #DC2626;
            }
        """)

        # Switch to User button - ADD THIS AFTER LOGOUT BUTTON
        self.switch_user_btn = QtWidgets.QPushButton("SWITCH TO USER", parent=self.top_frame)
        self.switch_user_btn.setGeometry(QtCore.QRect(560, 60, 100, 25))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)
        self.switch_user_btn.setFont(font_btn)
        self.switch_user_btn.setStyleSheet("""
            QPushButton {
                background-color: #10B981; 
                color: white; 
                border-radius: 5px;
                border: 2px solid #059669;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #059669;
            }
        """)


        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.main_frame.setStyleSheet("background-color: #e2d8f3;")
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")


        self.welcome_container = QtWidgets.QFrame(parent=self.main_frame)
        self.welcome_container.setGeometry(QtCore.QRect(50, 30, 671, 120))
        self.welcome_container.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: 3px solid #7C3AED;
            }
        """)


        self.welcome_label = QtWidgets.QLabel("Welcome back, Admin!", parent=self.welcome_container)
        self.welcome_label.setGeometry(QtCore.QRect(30, 20, 400, 30))
        welcome_font = QtGui.QFont()
        welcome_font.setFamily("Arial Black")
        welcome_font.setPointSize(20)
        welcome_font.setBold(True)
        self.welcome_label.setFont(welcome_font)
        self.welcome_label.setStyleSheet("color: #7C3AED;border: none; outline: none;")


        self.datetime_label = QtWidgets.QLabel(parent=self.welcome_container)
        self.datetime_label.setGeometry(QtCore.QRect(30, 60, 400, 25))
        datetime_font = QtGui.QFont()
        datetime_font.setFamily("Arial")
        datetime_font.setPointSize(12)
        self.datetime_label.setFont(datetime_font)
        self.datetime_label.setStyleSheet("color: #6B7280;border: none; outline: none;")


        self.status_label = QtWidgets.QLabel("🟢 All systems operational", parent=self.welcome_container)
        self.status_label.setGeometry(QtCore.QRect(30, 85, 300, 20))
        status_font = QtGui.QFont()
        status_font.setFamily("Arial")
        status_font.setPointSize(10)
        status_font.setBold(True)
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet("color: #059669;border: none; outline: none;")


        self.admin_icon = QtWidgets.QLabel("👨‍💼", parent=self.welcome_container)
        self.admin_icon.setGeometry(QtCore.QRect(550, 25, 80, 80))
        self.admin_icon.setStyleSheet("font-size: 60px;")
        self.admin_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


        self.stats_label = QtWidgets.QLabel("Quick Overview", parent=self.main_frame)
        self.stats_label.setGeometry(QtCore.QRect(50, 170, 200, 25))
        stats_title_font = QtGui.QFont()
        stats_title_font.setFamily("Arial Black")
        stats_title_font.setPointSize(16)
        stats_title_font.setBold(True)
        self.stats_label.setFont(stats_title_font)
        self.stats_label.setStyleSheet("color: black;")


        print("Setting up data cards...")


        self.stat_cards = []


        self.stats_container = QtWidgets.QWidget(parent=self.main_frame)
        self.stats_container.setGeometry(QtCore.QRect(50, 210, 671, 100))

        self.stats_layout = QtWidgets.QHBoxLayout(self.stats_container)
        self.stats_layout.setContentsMargins(0, 0, 0, 0)
        self.stats_layout.setSpacing(15)


        self.create_stat_card("Total Books", "📚", "0", "#7C3AED")
        self.create_stat_card("Active Users", "👥", "0", "#3B82F6")
        self.create_stat_card("Returned Books", "✅", "0", "#10B981")  # GREEN for returns
        self.create_stat_card("Overdue Books", "⏰", "0", "#EF4444")  # RED for overdue


        self.nav_label = QtWidgets.QLabel("Library Management", parent=self.main_frame)
        self.nav_label.setGeometry(QtCore.QRect(50, 330, 300, 25))
        nav_title_font = QtGui.QFont()
        nav_title_font.setFamily("Arial Black")
        nav_title_font.setPointSize(16)
        nav_title_font.setBold(True)
        self.nav_label.setFont(nav_title_font)
        self.nav_label.setStyleSheet("color: black;")


        self.nav_container = QtWidgets.QWidget(parent=self.main_frame)
        self.nav_container.setGeometry(QtCore.QRect(50, 370, 671, 180))

        self.nav_grid = QtWidgets.QGridLayout(self.nav_container)
        self.nav_grid.setContentsMargins(0, 0, 0, 0)
        self.nav_grid.setHorizontalSpacing(20)
        self.nav_grid.setVerticalSpacing(15)





        self.btn_books = self.create_nav_button("BOOKS", "Manage Library Collection", "📚", 0, 0)
        self.btn_transaction = self.create_nav_button("TRANSACTION", "Borrow & Return Books", "🔄", 0, 1)
        self.btn_users = self.create_nav_button("USERS", "User Management", "👥", 1, 0)
        self.btn_report = self.create_nav_button("REPORT", "View Reports & Analytics", "📊", 1, 1)

        main_base.setCentralWidget(self.centralwidget)


        self.logout_btn.clicked.connect(self.logout_action)
        self.btn_books.clicked.connect(self.open_books)
        self.btn_transaction.clicked.connect(self.open_transaction_window)
        self.btn_users.clicked.connect(self.open_users)
        self.btn_report.clicked.connect(self.open_report)
        self.switch_user_btn.clicked.connect(self.switch_to_user)


        self.update_datetime()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)  # Update every second


        self.stats_timer = QtCore.QTimer()
        self.stats_timer.timeout.connect(self.load_quick_stats)
        self.stats_timer.start(3000)  # Update stats every 3 seconds


        QtCore.QTimer.singleShot(500, self.load_quick_stats)

    def create_stat_card(self, title, icon, value, color):
        """Create a stat card"""
        try:
            card = QtWidgets.QFrame()
            card.setMinimumSize(150, 90)
            card.setMaximumSize(200, 90)
            card.setStyleSheet(f"""
                QFrame {{
                    background-color: {color};
                    border-radius: 10px;
                    border: 2px solid {color};
                }}
            """)

            card_layout = QtWidgets.QVBoxLayout(card)
            card_layout.setContentsMargins(15, 10, 15, 10)
            card_layout.setSpacing(5)


            top_layout = QtWidgets.QHBoxLayout()

            icon_label = QtWidgets.QLabel(icon)
            icon_label.setStyleSheet("font-size: 20px; color: white;")

            title_label = QtWidgets.QLabel(title)
            title_label.setStyleSheet("color: white; font-weight: bold; font-size: 10px;")
            title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

            top_layout.addWidget(icon_label)
            top_layout.addWidget(title_label)


            value_label = QtWidgets.QLabel(value)
            value_label.setStyleSheet("color: white; font-weight: bold; font-size: 24px;")
            value_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

            card_layout.addLayout(top_layout)
            card_layout.addWidget(value_label)

            self.stats_layout.addWidget(card)


            self.stat_cards.append(value_label)

            print(f"✅ Created card: {title}")

            return value_label
        except Exception as e:
            print(f"❌ Error creating stat card: {e}")
            return None

    def create_nav_button(self, title, description, icon, row, col):
        """Create a navigation button"""
        try:
            button = QtWidgets.QPushButton()
            button.setMinimumSize(300, 80)
            button.setMaximumSize(400, 80)
            button.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border-radius: 12px;
                    border: 2px solid #E5E7EB;
                    text-align: left;
                    padding: 15px;
                }
                QPushButton:hover {
                    border-color: #7C3AED;
                    background-color: white; /* Stay white on hover */
                }
                QPushButton:pressed {
                    background-color: #F3F4F6;
                }
                QPushButton * {
                    background-color: white; /* 👈 makes all child widgets opaque white */
                }
            """)

            button_layout = QtWidgets.QHBoxLayout(button)
            button_layout.setContentsMargins(20, 15, 20, 15)
            button_layout.setSpacing(15)


            icon_label = QtWidgets.QLabel(icon)
            icon_label.setStyleSheet("font-size: 30px;")
            icon_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


            text_widget = QtWidgets.QWidget()
            text_layout = QtWidgets.QVBoxLayout(text_widget)
            text_layout.setContentsMargins(0, 0, 0, 0)
            text_layout.setSpacing(2)

            title_label = QtWidgets.QLabel(title)
            title_label.setStyleSheet("""
                color: #1F2937; 
                font-weight: bold; 
                font-size: 14px;
                font-family: 'Arial Black';
            """)

            desc_label = QtWidgets.QLabel(description)
            desc_label.setStyleSheet("color: #6B7280; font-size: 10px;")
            desc_label.setWordWrap(True)

            text_layout.addWidget(title_label)
            text_layout.addWidget(desc_label)

            button_layout.addWidget(icon_label)
            button_layout.addWidget(text_widget)
            button_layout.addStretch()

            self.nav_grid.addWidget(button, row, col)
            return button

        except Exception as e:
            print(f"❌ Error creating nav button: {e}")
            return None

    def update_datetime(self):
        """Update the date and time display"""
        try:
            current_datetime = QtCore.QDateTime.currentDateTime()
            formatted_datetime = current_datetime.toString("dddd, MMMM d, yyyy • hh:mm AP")
            self.datetime_label.setText(formatted_datetime)
        except Exception as e:
            print(f"❌ Error updating datetime: {e}")

    def load_quick_stats(self):
        """Load quick statistics - COUNT HISTORICAL OVERDUES"""
        try:
            db = Database()

            print("🔄 Loading quick stats from database...")


            total_books = db.fetch_one("SELECT COUNT(*) as count FROM books")
            total_books_count = total_books['count'] if total_books else 0


            active_users = db.fetch_one("SELECT COUNT(*) as count FROM users WHERE status = 'Active'")
            active_users_count = active_users['count'] if active_users else 0


            returned = db.fetch_one("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'borrow' AND status = 'returned'
            """)
            returned_count = returned['count'] if returned else 0


            overdue = db.fetch_one("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'borrow' 
                AND status = 'returned'
                AND return_date > due_date
            """)
            overdue_count = overdue['count'] if overdue else 0

            print(
                f"📊 Final Counts - Books: {total_books_count}, Users: {active_users_count}, Returned: {returned_count}, Overdue: {overdue_count}")


            if hasattr(self, 'stat_cards') and len(self.stat_cards) >= 4:
                self.stat_cards[0].setText(str(total_books_count))
                self.stat_cards[1].setText(str(active_users_count))
                self.stat_cards[2].setText(str(returned_count))
                self.stat_cards[3].setText(str(overdue_count))

        except Exception as e:
            print(f"❌ Error loading quick stats: {e}")
            if hasattr(self, 'stat_cards'):
                for card in self.stat_cards:
                    if card:
                        card.setText("0")


    def open_books(self):
        try:
            from books_window import BooksWindow
            self.books_window = QtWidgets.QMainWindow()
            self.books_ui = BooksWindow()
            self.books_ui.setupUi(self.books_window)
            self.books_window.show()
        except Exception as e:
            print(f"❌ Error opening books window: {e}")
            self.show_error_message("Cannot open Books window")

    def open_transaction_window(self):
        try:
            from transaction_borrow_window import TransactionBorrowWindow
            self.transaction_window = QtWidgets.QMainWindow()
            self.ui_transaction = TransactionBorrowWindow()
            self.ui_transaction.setupUi(self.transaction_window)
            self.transaction_window.show()
        except Exception as e:
            print(f"❌ Error opening transaction window: {e}")
            self.show_error_message("Cannot open Transaction window")

    def open_users(self):
        try:
            from user_window import UsersWindow
            self.users_window = QtWidgets.QMainWindow()
            self.users_ui = UsersWindow()
            self.users_ui.setupUi(self.users_window)
            self.users_window.show()
        except Exception as e:
            print(f"❌ Error opening users window: {e}")
            self.show_error_message("Cannot open Users window")

    def open_report(self):
        try:
            from reports_window import ReportsWindow
            self.report_window = QtWidgets.QMainWindow()
            self.report_ui = ReportsWindow()
            self.report_ui.setupUi(self.report_window)
            self.report_window.show()
        except Exception as e:
            print(f"❌ Error opening report window: {e}")
            self.show_error_message("Cannot open Reports window")

    def show_error_message(self, message):
        """Show error message to user"""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()

    def logout_action(self):
        reply = QtWidgets.QMessageBox.question(
            None, "Logout", "Are you sure you want to logout?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No
        )
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            # Stop the timers
            if hasattr(self, 'timer'):
                self.timer.stop()
            if hasattr(self, 'stats_timer'):
                self.stats_timer.stop()
            QtWidgets.QApplication.quit()

    def debug_transaction_data(self):
        """Debug method to see what's actually in the transactions table"""
        try:
            db = Database()

            print("🔍 === TRANSACTION DATA DEBUG ===")

            # Check ALL transactions and their status
            all_transactions = db.fetch_all("""
                SELECT id, transaction_type, status, due_date, return_date, book_title, user_name
                FROM transactions 
                ORDER BY id
            """)

            print(f"Total transactions in database: {len(all_transactions)}")

            # Count by transaction type and status
            for trans in all_transactions:
                print(
                    f"   📝 ID {trans['id']}: {trans['transaction_type']} - Status: '{trans['status']}' - Book: '{trans['book_title']}' - Due: {trans['due_date']} - Returned: {trans['return_date']}")

            # Check what status values actually exist
            status_counts = db.fetch_all("""
                SELECT transaction_type, status, COUNT(*) as count 
                FROM transactions 
                GROUP BY transaction_type, status
            """)

            print("\n📊 Transaction Status Counts:")
            for count in status_counts:
                print(f"   {count['transaction_type']} - {count['status']}: {count['count']}")

            # Test the returned books query
            returned_test = db.fetch_all("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'return'
            """)
            print(f"\n✅ Books with transaction_type = 'return': {returned_test[0]['count'] if returned_test else 0}")

            returned_with_status = db.fetch_all("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'return' AND status = 'returned'
            """)
            print(
                f"✅ Books with transaction_type = 'return' AND status = 'returned': {returned_with_status[0]['count'] if returned_with_status else 0}")

            print("🔍 === END DEBUG ===")

        except Exception as e:
            print(f"❌ Debug error: {e}")

    def switch_to_user(self):
        """Switch to user login interface"""
        try:
            from user_login_window import UserLoginWindow
            self.user_login_window = QtWidgets.QMainWindow()
            self.user_login_ui = UserLoginWindow()
            self.user_login_ui.setupUi(self.user_login_window)
            self.user_login_window.show()

            # Close current admin window
            for widget in QtWidgets.QApplication.topLevelWidgets():
                if hasattr(widget, 'objectName') and widget.objectName() == "main_base":
                    widget.close()
                    break

        except Exception as e:
            print(f"❌ Error switching to user interface: {e}")
            self.show_error_message("Cannot switch to user interface")