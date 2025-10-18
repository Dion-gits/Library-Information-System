from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class UsersWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UsersWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.db = Database()

        # --- Top frame ---
        self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(-10, -40, 821, 101))
        self.top_frame.setStyleSheet("background-color: #E0B3FF;")
        self.logo = QtWidgets.QLabel(parent=self.top_frame)
        self.logo.setGeometry(QtCore.QRect(0, 20, 111, 111))
        self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))
        self.logo.setScaledContents(True)
        self.label = QtWidgets.QLabel(parent=self.top_frame)
        self.label.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setScaledContents(True)
        self.label_title = QtWidgets.QLabel("All USERS", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(380, 60, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: white;")

        # --- Frame for controls ---
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.frame_3.setStyleSheet("background-color: #e2d8f3; color: black;")

        # --- Search bar ---
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(450, 20, 211, 24))
        self.lineEdit.setStyleSheet("background-color: white; color: black")
        self.lineEdit.setPlaceholderText("Search user...")

        self.btn_search = QtWidgets.QPushButton("SEARCH", parent=self.frame_3)
        self.btn_search.setGeometry(QtCore.QRect(670, 20, 81, 25))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)
        self.btn_search.setFont(font_btn)
        self.btn_search.setStyleSheet("background-color: #7C3AED; color: white")

        self.btn_sort = QtWidgets.QPushButton("SORT", parent=self.frame_3)
        self.btn_sort.setGeometry(QtCore.QRect(310, 20, 81, 25))
        self.btn_sort.setFont(font_btn)
        self.btn_sort.setStyleSheet("background-color: #7C3AED; color: white")

        self.comboBox_2 = QtWidgets.QComboBox(parent=self.frame_3)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 20, 121, 25))
        self.comboBox_2.setStyleSheet("background-color: white; color: black;")
        self.comboBox_2.addItems(["Default", "ID", "Name", "Email", "Status"])

        # --- Table ---
        self.table = QtWidgets.QTableWidget(parent=self.frame_3)
        self.table.setGeometry(QtCore.QRect(150, 60, 611, 501))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID Number", "Name", "Email", "Status", "Fees"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #e2e8f0;
                background: white;
                border-radius: 6px;
                font-size: 14px;
                color: black;
            }
            QHeaderView::section {
                background-color: #7C3AED;
                font-weight: bold;
                padding: 6px;
                border: none;
                color: white;
            }
        """)

        # Load users from database
        self.load_users_from_database()

        # --- Sidebar buttons ---
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 111, 181))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(6)

        self.btn_add = QtWidgets.QPushButton("ADD")
        self.btn_add.setFont(font_btn)
        self.btn_add.setStyleSheet("background-color: #7C3AED; color: white")
        self.verticalLayout.addWidget(self.btn_add)

        self.btn_update = QtWidgets.QPushButton("UPDATE")
        self.btn_update.setFont(font_btn)
        self.btn_update.setStyleSheet("background-color: #7C3AED; color: white")
        self.verticalLayout.addWidget(self.btn_update)

        self.btn_delete = QtWidgets.QPushButton("DELETE")
        self.btn_delete.setFont(font_btn)
        self.btn_delete.setStyleSheet("background-color: #7C3AED; color: white")
        self.verticalLayout.addWidget(self.btn_delete)

        self.btn_manage_fees = QtWidgets.QPushButton("MANAGE FEES")
        self.btn_manage_fees.setFont(font_btn)
        self.btn_manage_fees.setStyleSheet("background-color: #7C3AED; color: white")
        self.verticalLayout.addWidget(self.btn_manage_fees)

        self.btn_back = QtWidgets.QPushButton("Go Back")
        self.btn_back.setFont(font_btn)
        self.btn_back.setStyleSheet("background-color: #7C3AED; color: white")
        self.verticalLayout.addWidget(self.btn_back)
        self.btn_back.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)

        # --- Connect actions ---
        self.btn_add.clicked.connect(self.open_add)
        self.btn_update.clicked.connect(self.open_update)
        self.btn_delete.clicked.connect(self.open_delete)
        self.btn_manage_fees.clicked.connect(self.open_manage_fees)
        self.btn_search.clicked.connect(self.search_action)
        self.btn_sort.clicked.connect(self.sort_action)

    def load_users_from_database(self):
        """Load users from MySQL database into table"""
        try:
            query = "SELECT user_id, full_name, email, status, fees FROM users ORDER BY full_name"
            users = self.db.fetch_all(query)

            self.table.setRowCount(len(users))
            for row, user in enumerate(users):
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['user_id']))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['full_name']))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['email']))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['status']))

                # Format fees with peso sign
                fees_item = QtWidgets.QTableWidgetItem(f"₱{user['fees']:.2f}")
                if user['fees'] > 0:
                    fees_item.setForeground(QtGui.QColor('red'))
                self.table.setItem(row, 4, fees_item)

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error loading users from database: {str(e)}")

    def search_action(self):
        keyword = self.lineEdit.text().strip()
        if keyword:
            try:
                query = """
                    SELECT user_id, full_name, email, status, fees
                    FROM users
                    WHERE user_id LIKE %s OR full_name LIKE %s OR email LIKE %s
                    ORDER BY full_name
                """
                search_term = f"%{keyword}%"
                users = self.db.fetch_all(query, (search_term, search_term, search_term))

                self.table.setRowCount(len(users))
                for row, user in enumerate(users):
                    self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['user_id']))
                    self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['full_name']))
                    self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['email']))
                    self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['status']))

                    fees_item = QtWidgets.QTableWidgetItem(f"₱{user['fees']:.2f}")
                    if user['fees'] > 0:
                        fees_item.setForeground(QtGui.QColor('red'))
                    self.table.setItem(row, 4, fees_item)

            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", f"Error searching users: {str(e)}")
        else:
            self.load_users_from_database()

    def sort_action(self):
        sort_by = self.comboBox_2.currentText()
        try:
            order_by = ""
            if sort_by == "ID":
                order_by = "user_id ASC"
            elif sort_by == "Name":
                order_by = "full_name ASC"
            elif sort_by == "Email":
                order_by = "email ASC"
            elif sort_by == "Status":
                order_by = "status ASC"
            else:
                order_by = "full_name ASC"

            query = f"SELECT user_id, full_name, email, status, fees FROM users ORDER BY {order_by}"
            users = self.db.fetch_all(query)

            self.table.setRowCount(len(users))
            for row, user in enumerate(users):
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['user_id']))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['full_name']))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['email']))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['status']))

                fees_item = QtWidgets.QTableWidgetItem(f"₱{user['fees']:.2f}")
                if user['fees'] > 0:
                    fees_item.setForeground(QtGui.QColor('red'))
                self.table.setItem(row, 4, fees_item)

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error sorting users: {str(e)}")

    def open_add(self):
        from add_user import AddUserWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = AddUserWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.destroyed.connect(self.load_users_from_database)

    def open_update(self):
        from update_user_window import UpdateUserWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = UpdateUserWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.destroyed.connect(self.load_users_from_database)

    def open_delete(self):
        from delete_user_window import DeleteUserWindow
        self.delete_window = QtWidgets.QMainWindow()
        self.ui_delete = DeleteUserWindow()
        self.ui_delete.setupUi(self.delete_window)
        self.delete_window.show()
        self.delete_window.destroyed.connect(self.load_users_from_database)

    def open_manage_fees(self):
        from manage_fees_window import ManageFeesWindow
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            user_id = self.table.item(selected_row, 0).text()
            user_name = self.table.item(selected_row, 1).text()
            user_data = {'id': user_id, 'name': user_name}

            self.fees_window = QtWidgets.QMainWindow()
            self.ui_fees = ManageFeesWindow()
            self.ui_fees.setupUi(self.fees_window, user_data)
            self.fees_window.show()
            self.fees_window.destroyed.connect(self.load_users_from_database)
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to manage fees!")