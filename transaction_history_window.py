from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database
import csv
from datetime import datetime


class TransactionHistoryWindow(object):
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
        self.pushButton_7.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: #5B21B6; color: white; border: 2px solid #4C1D95;")
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
        self.label_3.setGeometry(QtCore.QRect(70, 130, 200, 16))
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

        # Filter section
        self.label_filter = QtWidgets.QLabel(parent=self.frame_3)
        self.label_filter.setGeometry(QtCore.QRect(70, 190, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        self.label_filter.setFont(font)
        self.label_filter.setStyleSheet("color: black; background-color: transparent;")
        self.label_filter.setObjectName("label_filter")

        self.comboBox_filter = QtWidgets.QComboBox(parent=self.frame_3)
        self.comboBox_filter.setGeometry(QtCore.QRect(70, 210, 151, 22))
        self.comboBox_filter.setStyleSheet("background: white; color: black;")
        self.comboBox_filter.setObjectName("comboBox_filter")
        self.comboBox_filter.addItems(
            ["All Transactions", "Borrows Only", "Returns Only", "Active Only", "Overdue Only"])

        # Search section
        self.lineEdit_search = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit_search.setGeometry(QtCore.QRect(240, 210, 181, 22))
        self.lineEdit_search.setStyleSheet("background: white; color: black;")
        self.lineEdit_search.setPlaceholderText("Search by Book, User, or ID...")
        self.lineEdit_search.setObjectName("lineEdit_search")

        self.pushButton_search = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_search.setGeometry(QtCore.QRect(430, 210, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_search.setObjectName("pushButton_search")

        # History table
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_3)
        self.tableWidget.setGeometry(QtCore.QRect(70, 250, 621, 281))
        self.tableWidget.setStyleSheet("background: white; color: black;")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID", "Book", "User", "Type", "Borrow Date", "Due Date", "Return Date", "Status/Fine"])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setObjectName("tableWidget")

        # Export button
        self.pushButton_export = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_export.setGeometry(QtCore.QRect(550, 540, 141, 27))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_export.setFont(font)
        self.pushButton_export.setStyleSheet("background-color: #7C3AED; color: white")
        self.pushButton_export.setObjectName("pushButton_export")

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
        self.pushButton_7.clicked.connect(lambda: self.open_due_dates(MainWindow))
        self.pushButton_8.clicked.connect(lambda: self.go_back_to_main(MainWindow))
        self.pushButton_search.clicked.connect(self.search_history)
        self.pushButton_export.clicked.connect(self.export_history)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Load initial history
        self.load_transaction_history()

    def load_transaction_history(self, search_term="", filter_type="All Transactions"):
        """Load transaction history with optional search and filter"""
        try:
            query = """
                SELECT t.id, t.book_title, t.user_name, t.transaction_type, 
                       t.borrow_date, t.return_date, t.due_date, t.status, t.fine,
                       t.created_at
                FROM transactions t
                WHERE 1=1
            """
            params = []

            # Apply search filter
            if search_term:
                query += " AND (t.book_title LIKE %s OR t.user_name LIKE %s OR t.id = %s)"
                params.extend([f"%{search_term}%", f"%{search_term}%", search_term])

            # Apply transaction type filter
            if filter_type == "Borrows Only":
                query += " AND t.transaction_type = 'borrow'"
            elif filter_type == "Returns Only":
                query += " AND t.transaction_type = 'return'"
            elif filter_type == "Overdue Only":
                query += " AND t.status = 'overdue'"
            elif filter_type == "Active Only":
                query += " AND t.status = 'active'"

            query += " ORDER BY t.created_at DESC"

            transactions = Database().fetch_all(query, params)

            self.tableWidget.setRowCount(len(transactions))

            for row, trans in enumerate(transactions):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(trans['id'])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(trans['book_title']))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(trans['user_name']))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(trans['transaction_type'].title()))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(trans['borrow_date'] or '')))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(trans['due_date'] or '')))
                self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(trans['return_date'] or '')))

                # Status with fine information
                status_text = trans['status'].title()
                if trans['fine'] and float(trans['fine']) > 0:
                    status_text += f" (Fine: ${trans['fine']})"

                status_item = QtWidgets.QTableWidgetItem(status_text)

                # Color coding for status
                if trans['status'] == 'overdue':
                    status_item.setForeground(QtGui.QColor('red'))
                elif trans['status'] == 'active':
                    status_item.setForeground(QtGui.QColor('blue'))
                elif trans['status'] == 'returned':
                    status_item.setForeground(QtGui.QColor('green'))

                self.tableWidget.setItem(row, 7, status_item)

            self.tableWidget.resizeColumnsToContents()

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error loading transaction history: {str(e)}")

    def search_history(self):
        """Search transaction history"""
        search_term = self.lineEdit_search.text().strip()
        filter_type = self.comboBox_filter.currentText()
        self.load_transaction_history(search_term, filter_type)

    def export_history(self):
        """Export transaction history to CSV"""
        try:
            # Get all transactions for export
            query = """
                SELECT t.id, t.book_title, t.user_name, t.transaction_type, 
                       t.borrow_date, t.due_date, t.return_date, t.status, t.fine,
                       t.created_at
                FROM transactions t
                ORDER BY t.created_at DESC
            """
            transactions = Database().fetch_all(query)

            if not transactions:
                QtWidgets.QMessageBox.warning(None, "Warning", "No transactions to export!")
                return

            # Create filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"library_transactions_{timestamp}.csv"

            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['ID', 'Book', 'User', 'Type', 'Borrow Date', 'Due Date', 'Return Date', 'Status', 'Fine',
                              'Created At']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for trans in transactions:
                    writer.writerow({
                        'ID': trans['id'],
                        'Book': trans['book_title'],
                        'User': trans['user_name'],
                        'Type': trans['transaction_type'],
                        'Borrow Date': trans['borrow_date'],
                        'Due Date': trans['due_date'],
                        'Return Date': trans['return_date'],
                        'Status': trans['status'],
                        'Fine': trans['fine'],
                        'Created At': trans['created_at']
                    })

            QtWidgets.QMessageBox.information(None, "Success",
                                              f"Transaction history exported to:\n{filename}")

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error exporting history: {str(e)}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "BORROW"))
        self.pushButton_6.setText(_translate("MainWindow", "RETURN"))
        self.pushButton_7.setText(_translate("MainWindow", "DUE DATES"))
        self.pushButton_5.setText(_translate("MainWindow", "HISTORY"))
        self.pushButton_8.setText(_translate("MainWindow", "Go Back"))
        self.label_3.setText(_translate("MainWindow", "Transaction History"))
        self.label_5.setText(_translate("MainWindow", "View and export transaction records."))
        self.label_filter.setText(_translate("MainWindow", "Filter by:"))
        self.pushButton_search.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_export.setText(_translate("MainWindow", "Export to CSV"))
        self.label_4.setText(_translate("MainWindow", "TRANSACTION"))

    def open_borrow(self, MainWindow):
        from transaction_borrow_window import TransactionBorrowWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = TransactionBorrowWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

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

    def go_back_to_main(self, MainWindow):
        from main_ui import Main_ui
        self.main_window = QtWidgets.QMainWindow()
        self.main_ui = Main_ui()
        self.main_ui.setupUi(self.main_window)
        self.main_window.show()
        MainWindow.close()