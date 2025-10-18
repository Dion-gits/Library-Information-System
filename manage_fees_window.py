from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class ManageFeesWindow:
    def setupUi(self, MainWindow, user_data=None):
        MainWindow.setObjectName("ManageFeesWindow")
        MainWindow.resize(500, 400)
        MainWindow.setMinimumSize(QtCore.QSize(500, 400))
        MainWindow.setMaximumSize(QtCore.QSize(500, 400))
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

        # Name label
        self.label = QtWidgets.QLabel(parent=self.top_frame)
        self.label.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label.setScaledContents(True)
        self.label.setStyleSheet("background: transparent;")

        # Title
        self.label_title = QtWidgets.QLabel("MANAGE FEES", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(200, 60, 201, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("color: white;")

        # Main frame
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 500, 340))
        self.frame_3.setStyleSheet("background-color: #e2d8f3;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        # User info
        self.user_info_label = QtWidgets.QLabel(parent=self.frame_3)
        self.user_info_label.setGeometry(QtCore.QRect(50, 30, 400, 30))
        self.user_info_label.setStyleSheet("font-size: 16px; font-weight: bold; color: black;")
        self.user_info_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Current fees
        self.current_fees_label = QtWidgets.QLabel(parent=self.frame_3)
        self.current_fees_label.setGeometry(QtCore.QRect(50, 70, 400, 30))
        self.current_fees_label.setStyleSheet("font-size: 14px; color: black;")
        self.current_fees_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Payment amount
        self.payment_label = QtWidgets.QLabel("Payment Amount (₱):", parent=self.frame_3)
        self.payment_label.setGeometry(QtCore.QRect(50, 120, 150, 25))
        self.payment_label.setStyleSheet("font-weight: bold; color: black;")

        self.payment_input = QtWidgets.QLineEdit(parent=self.frame_3)
        self.payment_input.setGeometry(QtCore.QRect(200, 120, 150, 25))
        self.payment_input.setStyleSheet("background-color: white; color: black;")
        self.payment_input.setPlaceholderText("0.00")

        # Reactivate account checkbox
        self.reactivate_checkbox = QtWidgets.QCheckBox("Reactivate user account", parent=self.frame_3)
        self.reactivate_checkbox.setGeometry(QtCore.QRect(50, 160, 200, 25))
        # self.reactivate_checkbox.setStyleSheet("background: white;")
        self.reactivate_checkbox.setStyleSheet("color: black;")

        # Buttons
        self.process_btn = QtWidgets.QPushButton("PROCESS PAYMENT", parent=self.frame_3)
        self.process_btn.setGeometry(QtCore.QRect(150, 200, 200, 35))
        self.process_btn.setStyleSheet("background-color: green; color: white; font-weight: bold;")

        self.clear_btn = QtWidgets.QPushButton("CLEAR", parent=self.frame_3)
        self.clear_btn.setGeometry(QtCore.QRect(150, 250, 90, 30))
        self.clear_btn.setStyleSheet("background-color: red; color: white; font-weight: bold;")

        self.back_btn = QtWidgets.QPushButton("GO BACK", parent=self.frame_3)
        self.back_btn.setGeometry(QtCore.QRect(260, 250, 90, 30))
        self.back_btn.setStyleSheet("background-color: #7C3AED; color: white; font-weight: bold;")

        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons
        self.process_btn.clicked.connect(self.process_payment)
        self.clear_btn.clicked.connect(self.clear_form)
        self.back_btn.clicked.connect(MainWindow.close)

        # Load user data
        if user_data:
            self.load_user_data()

    def load_user_data(self):
        """Load user data including fees and status"""
        try:
            query = "SELECT full_name, fees, status FROM users WHERE user_id = %s"
            user = self.db.fetch_one(query, (self.user_data['id'],))

            if user:
                self.user_info_label.setText(f"User: {self.user_data['id']} - {user['full_name']}")
                self.current_fees_label.setText(f"Current Outstanding Fees: ₱{user['fees']:.2f}")

                # Check if account is deactivated
                if user['status'] == 'Not Active':
                    self.reactivate_checkbox.setChecked(True)
                    self.reactivate_checkbox.setEnabled(True)
                else:
                    self.reactivate_checkbox.setChecked(False)
                    self.reactivate_checkbox.setEnabled(user['fees'] > 0)

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error loading user data: {str(e)}")

    def process_payment(self):
        """Process fee payment and account reactivation"""
        try:
            payment_amount = self.payment_input.text().strip()

            if not payment_amount:
                QtWidgets.QMessageBox.warning(None, "Error", "Please enter payment amount!")
                return

            try:
                payment = float(payment_amount)
                if payment < 0:
                    QtWidgets.QMessageBox.warning(None, "Error", "Payment amount cannot be negative!")
                    return
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Error", "Please enter a valid payment amount!")
                return

            # Get current user data
            query = "SELECT fees, status FROM users WHERE user_id = %s"
            user = self.db.fetch_one(query, (self.user_data['id'],))

            if not user:
                QtWidgets.QMessageBox.warning(None, "Error", "User not found!")
                return

            current_fees = user['fees']

            if payment > current_fees:
                QtWidgets.QMessageBox.warning(None, "Error",
                                              f"Payment amount (₱{payment:.2f}) cannot exceed current fees (₱{current_fees:.2f})!")
                return

            # Calculate new fees
            new_fees = current_fees - payment

            # Prepare update query
            update_query = "UPDATE users SET fees = %s"
            params = [new_fees]

            # Reactivate account if requested and fees are cleared
            reactivate = self.reactivate_checkbox.isChecked()
            if reactivate and new_fees <= 0:
                update_query += ", status = 'Active'"

            update_query += " WHERE user_id = %s"
            params.append(self.user_data['id'])

            # Execute update
            if self.db.execute_query(update_query, params):
                message = f"Payment of ₱{payment:.2f} processed successfully!\nRemaining fees: ₱{new_fees:.2f}"
                if reactivate and new_fees <= 0:
                    message += "\nAccount has been reactivated!"

                QtWidgets.QMessageBox.information(None, "Success", message)
                self.clear_form()
                self.load_user_data()
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Failed to process payment!")

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error processing payment: {str(e)}")

    def clear_form(self):
        """Clear the payment form"""
        self.payment_input.clear()
        self.load_user_data()