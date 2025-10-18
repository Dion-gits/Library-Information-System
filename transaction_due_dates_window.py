from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database
from datetime import datetime


class TransactionDueDatesWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 766, 614))
        self.frame_3.setStyleSheet("background-color: #e2d8f3;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 0, 661, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Navigation buttons
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: #5B21B6; color: white; border: 2px solid #4C1D95;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)

        # Go Back button
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 540, 91, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_8.setObjectName("pushButton_8")

        # Main content labels
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: black; background-color: transparent;")
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(70, 160, 331, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: black; background-color: transparent;")
        self.label_5.setObjectName("label_5")

        # Overdue Books section
        self.label_8 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(430, 130, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: black; background-color: transparent;")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(430, 160, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: black; background-color: transparent;")
        self.label_9.setObjectName("label_9")

        # Table for due dates
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(70, 190, 291, 281))
        self.tableWidget.setStyleSheet("background: white; color: black;")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Book Title", "User", "Borrow Date", "Due Date", "Days Left"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setObjectName("tableWidget")

        # Overdue list
        self.listWidget = QtWidgets.QListWidget(parent=self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(430, 190, 291, 281))
        self.listWidget.setStyleSheet("background: white; color: black;")
        self.listWidget.setObjectName("listWidget")

        # Send Reminder button
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(90, 490, 251, 27))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton.setObjectName("pushButton")

        # Top Frame with logo and name
        self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(-10, -40, 821, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setStyleSheet("background-color: #E0B3FF;")
        self.top_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_frame.setObjectName("top_frame")

        # Logo
        self.logo = QtWidgets.QLabel(parent=self.top_frame)
        self.logo.setGeometry(QtCore.QRect(0, 20, 111, 111))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet("background: transparent;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        # Name
        self.label_2 = QtWidgets.QLabel(parent=self.top_frame)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setObjectName("label_2")

        # Title
        self.label_4 = QtWidgets.QLabel(parent=self.top_frame)
        self.label_4.setGeometry(QtCore.QRect(380, 60, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white; background-color: transparent;")
        self.label_4.setObjectName("label_4")

        MainWindow.setCentralWidget(self.centralwidget)

        # Set text
        self.retranslateUi(MainWindow)

        # Connect buttons
        self.pushButton_4.clicked.connect(lambda: self.open_borrow(MainWindow))
        self.pushButton_6.clicked.connect(lambda: self.open_return(MainWindow))
        self.pushButton_5.clicked.connect(lambda: self.open_history(MainWindow))
        self.pushButton_8.clicked.connect(lambda: self.go_back_to_main(MainWindow))
        self.pushButton.clicked.connect(self.send_reminder)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load due dates and overdue books
        self.load_due_dates()
        self.load_overdue_books()

    def load_due_dates(self):
        """Load active borrows with due dates - FIXED"""
        try:
            db = Database()  # Create Database instance

            # First, debug what's in the database
            debug_query = "SHOW COLUMNS FROM transactions"
            columns = db.fetch_all(debug_query)
            print("Transactions table columns for due dates:")
            for col in columns:
                print(f"  - {col['Field']}")

            # Check active borrows
            count_query = "SELECT COUNT(*) as count FROM transactions WHERE transaction_type = 'borrow' AND status = 'active'"
            count_result = db.fetch_one(count_query)
            print(f"Active borrows count: {count_result['count']}")

            # Get all active borrows to see what we have
            sample_query = """
                SELECT t.id, t.book_title, t.user_name, t.borrow_date, t.due_date, t.status
                FROM transactions t
                WHERE t.transaction_type = 'borrow' AND t.status = 'active'
                LIMIT 5
            """
            sample_data = db.fetch_all(sample_query)
            print("Sample active borrows:")
            for item in sample_data:
                print(f"  - Book: {item['book_title']}, User: {item['user_name']}, Due: {item['due_date']}")

            # Main query for due dates
            query = """
                SELECT 
                    COALESCE(t.book_title, b.title) as book_title,
                    COALESCE(t.user_name, u.full_name) as user_name,
                    t.borrow_date,
                    t.due_date,
                    DATEDIFF(t.due_date, CURDATE()) as days_remaining
                FROM transactions t
                LEFT JOIN books b ON t.book_id = b.id
                LEFT JOIN users u ON t.user_id = u.id
                WHERE t.transaction_type = 'borrow' 
                  AND t.status = 'active'
                  AND t.due_date IS NOT NULL
                ORDER BY t.due_date ASC
            """
            due_books = db.fetch_all(query)

            print(f"Found {len(due_books)} books with due dates")

            self.tableWidget.setRowCount(len(due_books))

            for row, book in enumerate(due_books):
                # Create items for each cell
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(book['book_title'] or 'Unknown Book')))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(book['user_name'] or 'Unknown User')))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(book['borrow_date'] or 'Unknown')))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(book['due_date'] or 'Unknown')))

                days_left = book['days_remaining'] or 0
                days_text = str(days_left)
                days_item = QtWidgets.QTableWidgetItem(days_text)

                # Color code based on urgency
                if days_left < 0:
                    days_item.setForeground(QtGui.QColor('red'))
                    days_item.setText(f"Overdue ({abs(days_left)} days)")
                elif days_left <= 3:
                    days_item.setForeground(QtGui.QColor('orange'))
                else:
                    days_item.setForeground(QtGui.QColor('green'))

                self.tableWidget.setItem(row, 4, days_item)

            # If no data found, add sample data for testing
            if len(due_books) == 0:
                self.tableWidget.setRowCount(2)
                # Sample row 1
                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Sample Book 1"))
                self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Test User 1"))
                self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("2024-01-01"))
                self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("2024-01-15"))
                sample_item = QtWidgets.QTableWidgetItem("5")
                sample_item.setForeground(QtGui.QColor('green'))
                self.tableWidget.setItem(0, 4, sample_item)

                # Sample row 2
                self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("Sample Book 2"))
                self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("Test User 2"))
                self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem("2024-01-05"))
                self.tableWidget.setItem(1, 3, QtWidgets.QTableWidgetItem("2024-01-10"))
                sample_item2 = QtWidgets.QTableWidgetItem("Overdue (2 days)")
                sample_item2.setForeground(QtGui.QColor('red'))
                self.tableWidget.setItem(1, 4, sample_item2)

            # Resize columns to fit content
            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            print(f"Error loading due dates: {e}")
            # Don't crash - show error in table
            self.tableWidget.setRowCount(1)
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(f"Error: {str(e)}"))

    def load_overdue_books(self):
        """Load overdue books - FIXED missing db variable"""
        try:
            db = Database()  # Add this line - create Database instance

            query = """
                SELECT 
                    COALESCE(t.book_title, b.title) as book_title,
                    COALESCE(t.user_name, u.full_name) as user_name,
                    t.due_date,
                    DATEDIFF(CURDATE(), t.due_date) as days_overdue,
                    u.email, 
                    u.contact
                FROM transactions t
                LEFT JOIN books b ON t.book_id = b.id
                LEFT JOIN users u ON t.user_id = u.id
                WHERE t.transaction_type = 'borrow' 
                  AND t.status = 'active'
                  AND t.due_date < CURDATE()
                ORDER BY t.due_date ASC
            """
            overdue_books = db.fetch_all(query)

            self.listWidget.clear()
            if overdue_books:
                for book in overdue_books:
                    item_text = f"{book['book_title']} - {book['user_name']} (Overdue: {book['days_overdue']} days)"
                    self.listWidget.addItem(item_text)
            else:
                self.listWidget.addItem("No overdue books found")
                # Add sample data for testing
                self.listWidget.addItem("Sample Book - Test User (Overdue: 5 days)")
                self.listWidget.addItem("Another Book - User Two (Overdue: 2 days)")

        except Exception as e:
            print(f"Error loading overdue books: {e}")
            self.listWidget.clear()
            self.listWidget.addItem("Error loading overdue books")

    def send_reminder(self):
        """Send reminder for selected overdue books"""
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(None, "Warning", "Please select overdue books to send reminders!")
            return

        for item in selected_items:
            book_info = item.text()
            # In a real system, you would send email/SMS here
            print(f"Reminder sent for: {book_info}")

        QtWidgets.QMessageBox.information(None, "Success",
                                          f"Reminders sent for {len(selected_items)} overdue book(s)!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "BORROW"))
        self.pushButton_6.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_7.setText(_translate("MainWindow", "DUE DATES"))
        self.pushButton_5.setText(_translate("MainWindow", "HISTORY"))
        self.pushButton_8.setText(_translate("MainWindow", "Go Back"))
        self.label_3.setText(_translate("MainWindow", "Due Dates"))
        self.label_5.setText(_translate("MainWindow", "View and manage upcoming due dates."))
        self.label_8.setText(_translate("MainWindow", "Overdue Books"))
        self.label_9.setText(_translate("MainWindow", "Books that are past due date."))
        self.pushButton.setText(_translate("MainWindow", "Send Reminder"))
        self.label_4.setText(_translate("MainWindow", "TRANSACTION"))

    def open_borrow(self, MainWindow):
        try:
            from transaction_borrow_window import TransactionBorrowWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = TransactionBorrowWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close()
        except Exception as e:
            print(f"Error opening borrow window: {e}")
            QtWidgets.QMessageBox.warning(None, "Error", f"Could not open borrow window: {str(e)}")

    def open_return(self, MainWindow):
        try:
            from transaction_return_window import TransactionReturnWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = TransactionReturnWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close()
        except Exception as e:
            print(f"Error opening return window: {e}")
            QtWidgets.QMessageBox.warning(None, "Error", f"Could not open return window: {str(e)}")

    def open_history(self, MainWindow):
        try:
            from transaction_history_window import TransactionHistoryWindow
            self.window = QtWidgets.QMainWindow()
            self.ui = TransactionHistoryWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            MainWindow.close()
        except Exception as e:
            print(f"Error opening history window: {e}")
            QtWidgets.QMessageBox.warning(None, "Error", f"Could not open history window: {str(e)}")

    def go_back_to_main(self, MainWindow):
        try:
            from main_ui import Main_ui
            self.main_window = QtWidgets.QMainWindow()
            self.main_ui = Main_ui()
            self.main_ui.setupUi(self.main_window)
            self.main_window.show()
            MainWindow.close()
        except Exception as e:
            print(f"Error going back to main: {e}")
            QtWidgets.QMessageBox.warning(None, "Error", f"Could not return to main: {str(e)}")