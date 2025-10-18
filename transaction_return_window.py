from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database
from datetime import datetime


class TransactionReturnWindow(object):
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
        self.pushButton_6.setStyleSheet("background-color: #5B21B6; color: white; border: 2px solid #4C1D95;")
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

        # Recent returns section
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

        # Return button
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(80, 440, 251, 27))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton.setObjectName("pushButton")

        # Input fields (Book ID and User ID)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 180, 281, 141))
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

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit_3.setStyleSheet("background: white; color: black;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

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

        # Fine field
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: black; background-color: transparent;")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)

        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("background: white; color: black;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("0.00")
        self.verticalLayout.addWidget(self.lineEdit)

        # Date fields
        self.label_13 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(70, 380, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: black; background-color: transparent;")
        self.label_13.setObjectName("label_13")

        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(70, 400, 111, 21))
        self.lineEdit_5.setStyleSheet("background: white; color: black;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.label_14 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(200, 400, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: black; background-color: transparent;")
        self.label_14.setObjectName("label_14")

        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 400, 111, 21))
        self.lineEdit_6.setStyleSheet("background: white; color: black;")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.label_11 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(240, 370, 81, 34))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: black; background-color: transparent;")
        self.label_11.setObjectName("label_11")

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
        self.pushButton_7.clicked.connect(lambda: self.open_due_dates(MainWindow))
        self.pushButton_5.clicked.connect(lambda: self.open_history(MainWindow))
        self.pushButton_8.clicked.connect(lambda: self.go_back_to_main(MainWindow))
        self.pushButton.clicked.connect(self.return_book)

        # Connect book ID field to auto-fill borrow date
        self.lineEdit_3.textChanged.connect(self.auto_fill_borrow_date)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set default return date and load recent returns
        self.lineEdit_6.setText(datetime.now().strftime("%Y-%m-%d"))
        self.load_recent_returns()

    def auto_fill_borrow_date(self):
        """Auto-fill borrow date when book ID is entered"""
        book_id = self.lineEdit_3.text().strip()
        user_id = self.lineEdit_2.text().strip()

        if book_id and user_id:
            try:
                db = Database()
                # Find active borrow transaction
                borrow_query = """
                    SELECT t.borrow_date 
                    FROM transactions t
                    JOIN books b ON t.book_id = b.id
                    JOIN users u ON t.user_id = u.id
                    WHERE b.id = %s AND u.user_id = %s AND t.transaction_type = 'borrow' AND t.status = 'active'
                """
                borrow = db.fetch_one(borrow_query, (int(book_id), user_id))

                if borrow:
                    self.lineEdit_5.setText(str(borrow['borrow_date']))
                else:
                    self.lineEdit_5.clear()
            except:
                self.lineEdit_5.clear()

    def load_recent_returns(self):
        """Load recent return transactions - FIXED with better query"""
        try:
            # First, let's check what's actually in the transactions table
            db = Database()

            # Debug: Check table structure and content
            debug_query = "SHOW COLUMNS FROM transactions"
            columns = db.fetch_all(debug_query)
            print("Transactions table columns:")
            for col in columns:
                print(f"  - {col['Field']}")

            # Check if we have any return transactions
            count_query = "SELECT COUNT(*) as count FROM transactions WHERE transaction_type = 'return'"
            count_result = db.fetch_one(count_query)
            print(f"Return transactions count: {count_result['count']}")

            # Get all transactions to see what we have
            all_query = "SELECT id, transaction_type, status, book_title, user_name FROM transactions LIMIT 10"
            all_transactions = db.fetch_all(all_query)
            print("Sample transactions:")
            for trans in all_transactions:
                print(
                    f"  - ID: {trans['id']}, Type: {trans['transaction_type']}, Status: {trans['status']}, Book: {trans['book_title']}")

            # Modified query to handle both old and new transaction structures
            query = """
                SELECT t.id, 
                       COALESCE(t.book_title, b.title) as book_title,
                       COALESCE(t.user_name, u.full_name) as user_name, 
                       t.return_date, 
                       COALESCE(t.fine, 0) as fine,
                       t.created_at
                FROM transactions t
                LEFT JOIN books b ON t.book_id = b.id
                LEFT JOIN users u ON t.user_id = u.id
                WHERE t.transaction_type = 'return' 
                   OR (t.transaction_type = 'borrow' AND t.status = 'returned')
                ORDER BY t.created_at DESC 
                LIMIT 10
            """
            returns = db.fetch_all(query)

            self.listWidget.clear()
            if returns:
                for return_trans in returns:
                    fine_text = f" - Fine: ₱{float(return_trans['fine']):.2f}" if return_trans['fine'] and float(
                        return_trans['fine']) > 0 else ""
                    return_date = return_trans['return_date'] or return_trans['created_at']
                    item_text = f"{return_trans['book_title']} - {return_trans['user_name']} (Returned: {return_date}{fine_text})"
                    self.listWidget.addItem(item_text)
            else:
                self.listWidget.addItem("No recent returns found")
                # Add sample data for testing
                self.listWidget.addItem("Sample Return 1 - Test User (Returned: 2024-01-15)")
                self.listWidget.addItem("Sample Return 2 - Test User 2 (Returned: 2024-01-14)")

        except Exception as e:
            print(f"Error loading recent returns: {e}")
            # Add a fallback message
            self.listWidget.clear()
            self.listWidget.addItem("Error loading recent returns - check console for details")

    def return_book(self):
        """Process book return with fine calculation - COMPLETELY REWRITTEN"""
        try:
            book_id = self.lineEdit_3.text().strip()
            user_id = self.lineEdit_2.text().strip()
            fine_amount = self.lineEdit.text().strip() or "0"
            return_date = self.lineEdit_6.text().strip()

            if not all([book_id, user_id, return_date]):
                QtWidgets.QMessageBox.warning(None, "Error", "Please fill in Book ID, User ID, and Return Date!")
                return

            db = Database()

            # Find book
            book = db.fetch_one("SELECT id, title, available FROM books WHERE id = %s", (int(book_id),))
            if not book:
                QtWidgets.QMessageBox.warning(None, "Error", "Book not found!")
                return

            # Find user
            user = db.fetch_one("SELECT id, full_name FROM users WHERE user_id = %s", (user_id,))
            if not user:
                QtWidgets.QMessageBox.warning(None, "Error", "User not found!")
                return

            # Find active borrow transaction
            borrow_query = """
                SELECT t.id, t.due_date, t.borrow_date
                FROM transactions t
                WHERE t.book_id = %s AND t.user_id = %s AND t.transaction_type = 'borrow' AND t.status = 'active'
            """
            borrow = db.fetch_one(borrow_query, (book['id'], user['id']))

            if not borrow:
                QtWidgets.QMessageBox.warning(None, "Error", "No active borrow found for this book and user!")
                return

            # Calculate fine if overdue
            days_overdue = 0
            calculated_fine = 0.0

            try:
                due_date = datetime.strptime(str(borrow['due_date']), '%Y-%m-%d')
                return_date_obj = datetime.strptime(return_date, '%Y-%m-%d')

                if return_date_obj > due_date:
                    days_overdue = (return_date_obj - due_date).days
                    calculated_fine = days_overdue * 1.00  # ₱1 per day
                    if float(fine_amount) != calculated_fine:
                        fine_amount = str(calculated_fine)
                        self.lineEdit.setText(fine_amount)
            except Exception as e:
                print(f"Error calculating fine: {e}")

            connection = db.connect()
            if connection:
                cursor = connection.cursor()
                try:
                    # OPTION 1: Update the existing borrow transaction
                    update_borrow_query = """
                        UPDATE transactions 
                        SET status = 'returned', 
                            return_date = %s, 
                            fine = %s
                        WHERE id = %s
                    """
                    cursor.execute(update_borrow_query, (return_date, float(fine_amount), borrow['id']))

                    # OPTION 2: Also create a new return transaction record
                    insert_return_query = """
                        INSERT INTO transactions (book_id, user_id, transaction_type, return_date, status, fine, book_title, user_name)
                        VALUES (%s, %s, 'return', %s, 'returned', %s, %s, %s)
                    """
                    cursor.execute(insert_return_query,
                                   (book['id'], user['id'], return_date, float(fine_amount), book['title'],
                                    user['full_name']))

                    # Update book availability
                    update_book_query = "UPDATE books SET available = available + 1 WHERE id = %s"
                    cursor.execute(update_book_query, (book['id'],))

                    # Update user fees if there's a fine
                    if float(fine_amount) > 0:
                        update_user_fees_query = "UPDATE users SET fees = fees + %s WHERE id = %s"
                        cursor.execute(update_user_fees_query, (float(fine_amount), user['id']))

                    connection.commit()

                    # Get updated available count
                    updated_book = db.fetch_one("SELECT available FROM books WHERE id = %s", (book['id'],))

                    message = f"Book '{book['title']}' returned successfully by {user['full_name']}!"
                    if float(fine_amount) > 0:
                        message += f"\nOverdue fine: ₱{float(fine_amount):.2f} (added to user's total fees)"

                    if updated_book['available'] > 0:
                        message += f"\nBook is now available (copies: {updated_book['available']})"

                    QtWidgets.QMessageBox.information(None, "Success", message)
                    self.clear_form()
                    self.load_recent_returns()

                except Exception as e:
                    connection.rollback()
                    QtWidgets.QMessageBox.warning(None, "Error", f"Error returning book: {str(e)}")
                finally:
                    cursor.close()
                    connection.close()

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error processing return: {str(e)}")

    def clear_form(self):
        """Clear the form"""
        self.lineEdit_3.clear()
        self.lineEdit_2.clear()
        self.lineEdit.setText("0.00")
        self.lineEdit_5.clear()
        # Keep return date as today
        self.lineEdit_6.setText(datetime.now().strftime("%Y-%m-%d"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "BORROW"))
        self.pushButton_6.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_7.setText(_translate("MainWindow", "DUE DATES"))
        self.pushButton_5.setText(_translate("MainWindow", "HISTORY"))
        self.pushButton_8.setText(_translate("MainWindow", "Go Back"))
        self.label_3.setText(_translate("MainWindow", "Return a Book"))
        self.label_5.setText(_translate("MainWindow", "Enter details to return book."))
        self.label_8.setText(_translate("MainWindow", "Recent Returns"))
        self.label_9.setText(_translate("MainWindow", "Recently returned book."))
        self.pushButton.setText(_translate("MainWindow", "Return"))
        self.label_7.setText(_translate("MainWindow", "Book ID:"))
        self.label_6.setText(_translate("MainWindow", "User ID:"))
        self.label_10.setText(_translate("MainWindow", "Fine:"))
        self.label_13.setText(_translate("MainWindow", "Borrowed Date:"))
        self.label_14.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", "Return Date:"))
        self.label_4.setText(_translate("MainWindow", "TRANSACTION"))

    def open_borrow(self, MainWindow):
        from transaction_borrow_window import TransactionBorrowWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = TransactionBorrowWindow()
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