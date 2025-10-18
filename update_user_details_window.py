from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class UpdateUserDetailsWindow:
    def setupUi(self, MainWindow, user_data=None, refresh_callback=None):
        MainWindow.setObjectName("UpdateUserDetailsWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_window = MainWindow
        self.user_data = user_data
        self.refresh_callback = refresh_callback
        self.db = Database()

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

        # System Name
        self.label_name = QtWidgets.QLabel(parent=self.top_frame)
        self.label_name.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label_name.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label_name.setStyleSheet("background-color: transparent;")
        self.label_name.setScaledContents(True)

        # Title
        self.label_title = QtWidgets.QLabel("UPDATE USER DETAILS", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(380, 60, 320, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("color: white;")

        # --- Main frame ---
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.frame_3.setStyleSheet("background-color: #e2d8f3; color: black;")

        # --- Form container ---
        self.form_container = QtWidgets.QFrame(parent=self.frame_3)
        self.form_container.setGeometry(QtCore.QRect(150, 70, 500, 400))
        self.form_container.setStyleSheet("""
            background-color: white;
            border-radius: 15px;
            border: 2px solid #7C3AED;
        """)

        self.formLayout = QtWidgets.QFormLayout(self.form_container)
        self.formLayout.setContentsMargins(30, 20, 30, 20)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setHorizontalSpacing(20)

        label_style = """
            QLabel {
                color: #374151;
                font-weight: bold;
                font-size: 12px;
                min-width: 120px;
            }
        """
        field_style = """
            QLineEdit {
                background-color: #FFFFFF;
                color: #1f2937;
                border: 2px solid #d1d5db;
                border-radius: 8px;
                padding: 10px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border-color: #7C3AED;
                background-color: #faf5ff;
            }
            QLineEdit[readOnly="true"] {
                background-color: #f3f4f6;
                color: #6b7280;
                border-color: #9ca3af;
            }
        """
        combo_style = """
            QComboBox {
                background-color: #FFFFFF;
                color: #1f2937;
                border: 2px solid #d1d5db;
                border-radius: 8px;
                padding: 10px;
                font-size: 12px;
            }
            QComboBox:focus {
                border-color: #7C3AED;
                background-color: #faf5ff;
            }
        """

        # Fields - Changed from book to user fields
        self.label_user_id = QtWidgets.QLabel("User ID:")
        self.label_user_id.setStyleSheet(label_style)
        self.lineEdit_user_id = QtWidgets.QLineEdit()
        self.lineEdit_user_id.setReadOnly(True)
        self.lineEdit_user_id.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_user_id, self.lineEdit_user_id)

        self.label_full_name = QtWidgets.QLabel("Full Name:")
        self.label_full_name.setStyleSheet(label_style)
        self.lineEdit_full_name = QtWidgets.QLineEdit()
        self.lineEdit_full_name.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_full_name, self.lineEdit_full_name)

        self.label_age = QtWidgets.QLabel("Age:")
        self.label_age.setStyleSheet(label_style)
        self.lineEdit_age = QtWidgets.QLineEdit()
        self.lineEdit_age.setStyleSheet(field_style)
        self.lineEdit_age.setPlaceholderText("e.g., 25")
        self.formLayout.addRow(self.label_age, self.lineEdit_age)

        self.label_password = QtWidgets.QLabel("Password:")
        self.label_password.setStyleSheet(label_style)
        self.lineEdit_password = QtWidgets.QLineEdit()
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_password, self.lineEdit_password)

        self.label_email = QtWidgets.QLabel("Email:")
        self.label_email.setStyleSheet(label_style)
        self.lineEdit_email = QtWidgets.QLineEdit()
        self.lineEdit_email.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_email, self.lineEdit_email)

        self.label_contact = QtWidgets.QLabel("Contact:")
        self.label_contact.setStyleSheet(label_style)
        self.lineEdit_contact = QtWidgets.QLineEdit()
        self.lineEdit_contact.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_contact, self.lineEdit_contact)

        self.label_address = QtWidgets.QLabel("Address:")
        self.label_address.setStyleSheet(label_style)
        self.lineEdit_address = QtWidgets.QLineEdit()
        self.lineEdit_address.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_address, self.lineEdit_address)

        self.label_status = QtWidgets.QLabel("Status:")
        self.label_status.setStyleSheet(label_style)
        self.comboBox_status = QtWidgets.QComboBox()
        self.comboBox_status.addItems(["Active", "Not Active"])
        self.comboBox_status.setStyleSheet(combo_style)
        self.formLayout.addRow(self.label_status, self.comboBox_status)

        self.label_fees = QtWidgets.QLabel("Fees:")
        self.label_fees.setStyleSheet(label_style)
        self.lineEdit_fees = QtWidgets.QLineEdit()
        self.lineEdit_fees.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_fees, self.lineEdit_fees)

        # --- Buttons ---
        self.button_container = QtWidgets.QWidget(parent=self.frame_3)
        self.button_container.setGeometry(QtCore.QRect(150, 490, 500, 50))
        self.button_layout = QtWidgets.QHBoxLayout(self.button_container)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setSpacing(20)

        button_style = """
            QPushButton {
                border: none;
                border-radius: 8px;
                padding: 12px 25px;
                font-weight: bold;
                font-size: 12px;
                min-width: 100px;
            }
            QPushButton:hover {
                opacity: 0.9;
            }
        """

        # Create and style buttons
        self.pushButton_clear = QtWidgets.QPushButton("CLEAR")
        self.pushButton_clear.setStyleSheet(button_style + """
            QPushButton {
                background-color: #dc2626;
                color: white;
            }
            QPushButton:hover {
                background-color: #b91c1c;
            }
        """)

        self.pushButton_update = QtWidgets.QPushButton("UPDATE")
        self.pushButton_update.setStyleSheet(button_style + """
            QPushButton {
                background-color: #059669;
                color: white;
            }
            QPushButton:hover {
                background-color: #047857;
            }
        """)

        self.pushButton_go_back = QtWidgets.QPushButton("GO BACK")
        self.pushButton_go_back.setStyleSheet(button_style + """
            QPushButton {
                background-color: #7C3AED;
                color: white;
            }
            QPushButton:hover {
                background-color: #6d28d9;
            }
        """)

        self.button_layout.addWidget(self.pushButton_clear)
        self.button_layout.addWidget(self.pushButton_update)
        self.button_layout.addWidget(self.pushButton_go_back)

        MainWindow.setCentralWidget(self.centralwidget)

        # --- Connect and populate ---
        if user_data:
            self.prefill_form(user_data)
        self.pushButton_clear.clicked.connect(self.clear_form)
        self.pushButton_update.clicked.connect(self.update_user)
        self.pushButton_go_back.clicked.connect(MainWindow.close)

        self.set_tab_order()

    def set_tab_order(self):
        """Set proper tab order for form navigation"""
        QtWidgets.QWidget.setTabOrder(self.lineEdit_full_name, self.lineEdit_age)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_age, self.lineEdit_password)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_password, self.lineEdit_email)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_email, self.lineEdit_contact)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_contact, self.lineEdit_address)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_address, self.comboBox_status)
        QtWidgets.QWidget.setTabOrder(self.comboBox_status, self.lineEdit_fees)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_fees, self.pushButton_update)
        QtWidgets.QWidget.setTabOrder(self.pushButton_update, self.pushButton_clear)
        QtWidgets.QWidget.setTabOrder(self.pushButton_clear, self.pushButton_go_back)

    def prefill_form(self, user_data):
        """Pre-fill the form with the selected user's data"""
        try:
            if user_data:
                # Fetch complete user data from database
                user = self.db.fetch_one(
                    "SELECT * FROM users WHERE user_id = %s",
                    (user_data["user_id"],)
                )
                if user:
                    self.lineEdit_user_id.setText(user.get('user_id', ''))
                    self.lineEdit_full_name.setText(user.get('full_name', ''))
                    self.lineEdit_age.setText(str(user.get('age', '')))
                    self.lineEdit_password.setText(user.get('password', ''))
                    self.lineEdit_email.setText(user.get('email', ''))
                    self.lineEdit_contact.setText(user.get('contact', ''))
                    self.lineEdit_address.setText(user.get('address', ''))
                    self.lineEdit_fees.setText(str(user.get('fees', '0.00')))

                    # Set status
                    status = user.get('status', 'Active')
                    idx = self.comboBox_status.findText(status)
                    if idx >= 0:
                        self.comboBox_status.setCurrentIndex(idx)
        except Exception as e:
            self.show_error_message(f"Error loading user data: {str(e)}")

    def clear_form(self):
        """Clear all form fields except User ID"""
        self.lineEdit_full_name.clear()
        self.lineEdit_age.clear()
        self.lineEdit_password.clear()
        self.lineEdit_email.clear()
        self.lineEdit_contact.clear()
        self.lineEdit_address.clear()
        self.lineEdit_fees.clear()
        self.comboBox_status.setCurrentIndex(0)

    def validate_fields(self):
        """Validate all form fields before updating"""
        full_name = self.lineEdit_full_name.text().strip()
        age = self.lineEdit_age.text().strip()
        password = self.lineEdit_password.text().strip()
        email = self.lineEdit_email.text().strip()
        contact = self.lineEdit_contact.text().strip()
        address = self.lineEdit_address.text().strip()
        fees = self.lineEdit_fees.text().strip()

        # Check required fields
        if not all([full_name, age, password, email, contact, address, fees]):
            return False, "Please fill in all required fields!"

        # Validate age
        try:
            age_int = int(age)
            if age_int <= 0 or age_int > 120:
                return False, "Age must be between 1 and 120!"
        except ValueError:
            return False, "Age must be a valid number!"

        # Validate email format (basic validation)
        if "@" not in email or "." not in email:
            return False, "Please enter a valid email address!"

        # Validate fees
        try:
            fees_float = float(fees)
            if fees_float < 0:
                return False, "Fees cannot be negative!"
        except ValueError:
            return False, "Fees must be a valid number!"

        return True, "All fields are valid"

    def update_user(self):
        """Update user in database"""
        try:
            # Validate fields first
            is_valid, error_message = self.validate_fields()
            if not is_valid:
                self.show_error_message(error_message)
                return

            # Get form data
            user_id = self.lineEdit_user_id.text().strip()
            full_name = self.lineEdit_full_name.text().strip()
            age = self.lineEdit_age.text().strip()
            password = self.lineEdit_password.text().strip()
            email = self.lineEdit_email.text().strip()
            contact = self.lineEdit_contact.text().strip()
            address = self.lineEdit_address.text().strip()
            fees = self.lineEdit_fees.text().strip()
            status = self.comboBox_status.currentText()

            # Check if user ID exists
            if not user_id:
                self.show_error_message("No user selected for update!")
                return

            # Update user in database
            query = """
                UPDATE users 
                SET full_name = %s, age = %s, password = %s, email = %s, 
                    contact = %s, address = %s, status = %s, fees = %s
                WHERE user_id = %s
            """
            params = (full_name, int(age), password, email, contact, address, status, float(fees), user_id)

            # Show confirmation dialog
            reply = QtWidgets.QMessageBox.question(
                self.main_window,
                "Confirm Update",
                f"Are you sure you want to update user '{full_name}'?",
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )

            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                result = self.db.execute_query(query, params)

                if result:
                    self.show_success_message(f"User '{full_name}' updated successfully!")
                    # Call refresh callback if provided
                    if self.refresh_callback:
                        self.refresh_callback()
                else:
                    self.show_error_message("Failed to update user in database. Please try again.")

        except Exception as e:
            self.show_error_message(f"Error updating user: {str(e)}")

    def show_success_message(self, message):
        """Show success message"""
        msg = QtWidgets.QMessageBox(self.main_window)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    def show_error_message(self, message):
        """Show error message"""
        msg = QtWidgets.QMessageBox(self.main_window)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()