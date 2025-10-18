from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database
from datetime import datetime, timedelta


class TransactionBorrowWindow(object):
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
        self.pushButton_4.setStyleSheet("background-color: #5B21B6; color: white; border: 2px solid #4C1D95;")
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
        self.pushButton_7.setStyleSheet("background-color: #7C3AED; color: white")
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

        # Recent borrows section
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

        self.listWidget = QtWidgets.QListWidget(parent=self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(430, 190, 291, 281))
        self.listWidget.setStyleSheet("background: white; color: black;")
        self.listWidget.setObjectName("listWidget")

        # Borrow button
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(90, 410, 251, 27))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton.setObjectName("pushButton")

        # Date fields
        self.label_10 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(70, 350, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: black; background-color: transparent;")
        self.label_10.setObjectName("label_10")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 370, 111, 21))
        self.lineEdit_3.setStyleSheet("background: white; color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_11 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(250, 340, 81, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: black; background-color: transparent;")
        self.label_11.setObjectName("label_11")

        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 370, 111, 21))
        self.lineEdit_4.setStyleSheet("background: white; color: black;")
        self.lineEdit_4.setObjectName("lineEdit_4")

        # Input fields (Book ID and User ID)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 180, 291, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: black; background-color: transparent;")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("background: white; color: black;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: black; background-color: transparent;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("background: white; color: black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_12 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(210, 370, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: black; background-color: transparent;")
        self.label_12.setObjectName("label_12")

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
        self.pushButton_6.clicked.connect(lambda: self.open_return(MainWindow))
        self.pushButton_7.clicked.connect(lambda: self.open_due_dates(MainWindow))
        self.pushButton_5.clicked.connect(lambda: self.open_history(MainWindow))
        self.pushButton_8.clicked.connect(lambda: self.go_back_to_main(MainWindow))
        self.pushButton.clicked.connect(self.borrow_book)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set default dates and load recent borrows
        self.set_default_dates()
        self.load_recent_borrows()

    def set_default_dates(self):
        today = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
        self.lineEdit_3.setText(today)
        self.lineEdit_4.setText(due_date)

    def load_recent_borrows(self):
        """Load recent borrow transactions - FIXED"""
        try:
            query = """
                SELECT t.id, t.book_title, t.user_name, t.borrow_date, t.due_date 
                FROM transactions t
                WHERE t.transaction_type = 'borrow'
                ORDER BY t.created_at DESC LIMIT 10
            """
            borrows = Database().fetch_all(query)

            self.listWidget.clear()
            for borrow in borrows:
                item_text = f"{borrow['book_title']} - {borrow['user_name']} (Due: {borrow['due_date']})"
                self.listWidget.addItem(item_text)

            if not borrows:
                self.listWidget.addItem("No recent borrows found")

        except Exception as e:
            print(f"Error loading recent borrows: {e}")
            self.listWidget.clear()
            self.listWidget.addItem("Error loading recent borrows")

    def borrow_book(self):
        """Process book borrowing with enhanced validation - FIXED"""
        try:
            book_id = self.lineEdit.text().strip()
            user_id = self.lineEdit_2.text().strip()
            borrow_date = self.lineEdit_3.text().strip()
            due_date = self.lineEdit_4.text().strip()

            if not all([book_id, user_id, borrow_date, due_date]):
                QtWidgets.QMessageBox.warning(None, "Error", "Please fill in all fields!")
                return

            db = Database()

            # Check if book exists and is available
            book_query = "SELECT id, title, available, quantity FROM books WHERE id = %s"
            book = db.fetch_one(book_query, (int(book_id),))

            if not book:
                QtWidgets.QMessageBox.warning(None, "Error", "Book not found!")
                return

            # MODIFIED: Only prevent borrowing if NO copies are available
            if book['available'] <= 0:
                QtWidgets.QMessageBox.warning(None, "Error", "Book is not available for borrowing!")
                return

            # Check if user exists
            user_query = "SELECT id, full_name FROM users WHERE user_id = %s AND status = 'Active'"
            user = db.fetch_one(user_query, (user_id,))

            if not user:
                QtWidgets.QMessageBox.warning(None, "Error", "User not found or inactive!")
                return

            # Check if user already has this book borrowed
            existing_borrow_query = """
                SELECT id FROM transactions 
                WHERE book_id = %s AND user_id = %s AND transaction_type = 'borrow' AND status = 'active'
            """
            existing_borrow = db.fetch_one(existing_borrow_query, (book['id'], user['id']))

            if existing_borrow:
                QtWidgets.QMessageBox.warning(None, "Error", "User has already borrowed this book!")
                return

            # Create borrow transaction
            transaction_query = """
                INSERT INTO transactions (book_id, user_id, transaction_type, borrow_date, due_date, status, book_title, user_name)
                VALUES (%s, %s, 'borrow', %s, %s, 'active', %s, %s)
            """

            # Update book availability
            update_book_query = "UPDATE books SET available = available - 1 WHERE id = %s"

            connection = db.connect()
            if connection:
                cursor = connection.cursor()
                try:
                    # Insert transaction
                    cursor.execute(transaction_query,
                                   (book['id'], user['id'], borrow_date, due_date, book['title'], user['full_name']))
                    # Update book availability
                    cursor.execute(update_book_query, (book['id'],))
                    connection.commit()

                    # Get updated available count
                    updated_book = db.fetch_one("SELECT available FROM books WHERE id = %s", (book['id'],))

                    message = f"Book '{book['title']}' borrowed successfully by {user['full_name']}!\nDue Date: {due_date}"
                    if updated_book['available'] > 0:
                        message += f"\nCopies still available: {updated_book['available']}"
                    else:
                        message += f"\nNo copies available - book is now marked as 'Not Available'"

                    QtWidgets.QMessageBox.information(None, "Success", message)
                    self.clear_form()
                    self.load_recent_borrows()

                except Exception as e:
                    connection.rollback()
                    QtWidgets.QMessageBox.warning(None, "Error", f"Error borrowing book: {str(e)}")
                finally:
                    cursor.close()
                    connection.close()

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error processing borrow: {str(e)}")

    def clear_form(self):
        """Clear the form but keep dates"""
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.set_default_dates()

    def test_database_connection(self):
        """Test database connection and data retrieval"""
        try:
            db = Database()
            # Test borrows query
            borrows_query = "SELECT COUNT(*) as count FROM transactions WHERE transaction_type = 'borrow'"
            borrows_count = db.fetch_one(borrows_query)
            print(f"Borrows in database: {borrows_count['count']}")

            return True
        except Exception as e:
            print(f"Database test failed: {e}")
            return False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "BORROW"))
        self.pushButton_6.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_7.setText(_translate("MainWindow", "DUE DATES"))
        self.pushButton_5.setText(_translate("MainWindow", "HISTORY"))
        self.pushButton_8.setText(_translate("MainWindow", "Go Back"))
        self.label_3.setText(_translate("MainWindow", "Borrow a Book"))
        self.label_5.setText(_translate("MainWindow", "Enter details to process a new book loan."))
        self.label_8.setText(_translate("MainWindow", "Recent Borrows"))
        self.label_9.setText(_translate("MainWindow", "Recently completed book loans."))
        self.pushButton.setText(_translate("MainWindow", "Borrow"))
        self.label_10.setText(_translate("MainWindow", "Borrowed Date:"))
        self.label_11.setText(_translate("MainWindow", "Return Date:"))
        self.label_7.setText(_translate("MainWindow", "Book ID:"))
        self.label_6.setText(_translate("MainWindow", "User ID:"))
        self.label_12.setText(_translate("MainWindow", "-"))
        self.label_4.setText(_translate("MainWindow", "TRANSACTION"))

    def open_return(self, MainWindow):
        from transaction_return_window import TransactionReturnWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = TransactionReturnWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def open_due_dates(self, MainWindow):
        from transaction_due_dates_window import TransactionDueDatesWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = TransactionDueDatesWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def open_history(self, MainWindow):
        from transaction_history_window import TransactionHistoryWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = TransactionHistoryWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def go_back_to_main(self, MainWindow):
        from main_ui import Main_ui
        self.main_window = QtWidgets.QMainWindow()
        self.main_ui = Main_ui()
        self.main_ui.setupUi(self.main_window)
        self.main_window.show()
        MainWindow.close()