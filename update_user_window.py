from PyQt6 import QtCore, QtGui, QtWidgets


# NO top-level imports to prevent circular dependencies

class UpdateUserWindow:
    def setupUi(self, MainWindow):
        print("UpdateUserWindow: Starting setupUi")

        try:
            MainWindow.setObjectName("UpdateUserWindow")
            MainWindow.resize(766, 637)
            MainWindow.setMinimumSize(QtCore.QSize(766, 637))
            MainWindow.setMaximumSize(QtCore.QSize(766, 637))
            MainWindow.setStyleSheet("background-color: #ffffff;")

            self.centralwidget = QtWidgets.QWidget(parent=MainWindow)

            # --- Top frame ---
            self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
            self.top_frame.setGeometry(QtCore.QRect(-10, -40, 821, 101))
            self.top_frame.setStyleSheet("background-color: #E0B3FF;")

            # Logo
            self.logo = QtWidgets.QLabel(parent=self.top_frame)
            self.logo.setGeometry(QtCore.QRect(0, 20, 111, 111))
            self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))
            self.logo.setScaledContents(True)
            self.logo.setStyleSheet("background: transparent;")

            # Name label
            self.label = QtWidgets.QLabel(parent=self.top_frame)
            self.label.setGeometry(QtCore.QRect(70, 30, 141, 91))
            self.label.setPixmap(QtGui.QPixmap("logofff/name1.png"))
            self.label.setStyleSheet("background-color: transparent;")
            self.label.setScaledContents(True)

            self.label_title = QtWidgets.QLabel("UPDATE USER", parent=self.top_frame)
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
            self.table.setColumnCount(4)
            self.table.setHorizontalHeaderLabels(["ID Number", "Name", "Email", "Status"])
            self.table.horizontalHeader().setStretchLastSection(True)
            self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.table.setStyleSheet("""
                QTableWidget { 
                    border: 1px solid #e2e8f0; 
                    background: white; 
                    border-radius: 6px; 
                    font-size: 14px; 
                    color: black; 
                    selection-background-color: #d6e4ff;
                }
                QHeaderView::section { 
                    background-color: #e2e8f0; 
                    font-weight: bold; 
                    padding: 6px; 
                    border: none; 
                    color: black; 
                }
            """)

            # Enable row selection
            self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
            self.table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

            # --- Sidebar buttons ---
            self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
            self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 111, 181))
            self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
            self.verticalLayout.setContentsMargins(10, 0, 10, 0)
            self.verticalLayout.setSpacing(6)

            self.btn_select = QtWidgets.QPushButton("SELECT USER")
            self.btn_select.setFont(font_btn)
            self.btn_select.setStyleSheet("background-color: #7C3AED; color: white")
            self.verticalLayout.addWidget(self.btn_select)

            self.btn_back = QtWidgets.QPushButton("Go Back")
            self.btn_back.setFont(font_btn)
            self.btn_back.setStyleSheet("background-color: #7C3AED; color: white")
            self.verticalLayout.addWidget(self.btn_back)
            self.btn_back.clicked.connect(MainWindow.close)

            MainWindow.setCentralWidget(self.centralwidget)

            # --- Connect actions ---
            self.btn_search.clicked.connect(self.search_action)
            self.btn_sort.clicked.connect(self.sort_action)
            self.btn_select.clicked.connect(self.select_user)
            self.table.doubleClicked.connect(self.select_user)

            # Load users when window opens
            self.load_users()

            print("UpdateUserWindow: setupUi completed successfully")

        except Exception as e:
            print(f"UpdateUserWindow: Error in setupUi - {e}")
            raise

    def load_users(self, search_term=""):
        """Load users from database into table"""
        try:
            # Import database locally
            from database import Database
            db = Database()

            if search_term:
                query = """
                    SELECT user_id, full_name, email, status 
                    FROM users 
                    WHERE user_id LIKE %s OR full_name LIKE %s OR email LIKE %s
                    ORDER BY full_name
                """
                search_param = f"%{search_term}%"
                users = db.fetch_all(query, (search_param, search_param, search_param))
            else:
                query = "SELECT user_id, full_name, email, status FROM users ORDER BY full_name"
                users = db.fetch_all(query)

            self.table.setRowCount(len(users))
            for row, user in enumerate(users):
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(user['user_id']))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(user['full_name']))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(user['email']))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(user['status']))

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error loading users: {str(e)}")

    def get_selected_user_data(self):
        """Get data of selected user from table"""
        current_row = self.table.currentRow()
        if current_row >= 0:
            try:
                user_id = self.table.item(current_row, 0).text()
                user_name = self.table.item(current_row, 1).text()
                user_email = self.table.item(current_row, 2).text()

                return {
                    'id': user_id,
                    'name': user_name,
                    'email': user_email
                }
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", f"Error getting user data: {str(e)}")
        return None

    def select_user(self):
        """Open update details window for selected user"""
        user_data = self.get_selected_user_data()
        if user_data:
            # Import locally to avoid circular imports
            from update_user_details_window import UpdateUserDetailsWindow

            self.update_details_window = QtWidgets.QMainWindow()
            self.update_details_ui = UpdateUserDetailsWindow()
            self.update_details_ui.setupUi(self.update_details_window, user_data)
            self.update_details_window.show()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a user to update!")

    def search_action(self):
        """Search users in database"""
        search_text = self.lineEdit.text().strip()
        self.load_users(search_text)

    def sort_action(self):
        """Sort users table"""
        sort_by = self.comboBox_2.currentText()
        try:
            if sort_by == "ID":
                self.sort_table(0)  # Sort by ID column
            elif sort_by == "Name":
                self.sort_table(1)  # Sort by Name column
            elif sort_by == "Email":
                self.sort_table(2)  # Sort by Email column
            elif sort_by == "Status":
                self.sort_table(3)  # Sort by Status column
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error sorting: {str(e)}")

    def sort_table(self, column_index):
        """Sort table by specific column"""
        self.table.sortItems(column_index)