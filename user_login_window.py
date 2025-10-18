# user_login_window.py
from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class UserLoginWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UserLoginWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Top Frame
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

        # Name
        self.label_name = QtWidgets.QLabel(parent=self.top_frame)
        self.label_name.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label_name.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label_name.setScaledContents(True)
        self.label_name.setStyleSheet("background: transparent;")

        # Title
        self.label_title = QtWidgets.QLabel("LIBRARY USER LOGIN", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(300, 60, 281, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("color: white;")

        # Main Frame
        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.main_frame.setStyleSheet("background-color: #e2d8f3;")
        self.main_frame.setObjectName("main_frame")

        # Login Form Frame
        self.login_frame = QtWidgets.QFrame(parent=self.main_frame)
        self.login_frame.setGeometry(QtCore.QRect(200, 100, 400, 350))
        self.login_frame.setStyleSheet("""
            QFrame {
                background-color: #F3F4F6;
                border-radius: 20px;
                border: 3px solid #10B981;
            }
        """)

        # User Icon
        self.user_icon = QtWidgets.QLabel("👤", parent=self.login_frame)
        self.user_icon.setGeometry(QtCore.QRect(150, 20, 100, 100))
        self.user_icon.setStyleSheet("""
            font-size: 80px;
            border: none;
            background: transparent;
        """)
        self.user_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Form Widget
        self.form_widget = QtWidgets.QWidget(parent=self.login_frame)
        self.form_widget.setGeometry(QtCore.QRect(50, 130, 300, 150))
        self.form_widget.setStyleSheet("""
            QWidget {
                background-color: #F3F4F6;  /* same as login_frame */
                border-radius: 10px;
            }
        """)

        # User ID/Email
        self.label_user_id = QtWidgets.QLabel("User ID or Email:", parent=self.form_widget)
        self.label_user_id.setGeometry(QtCore.QRect(0, 0, 150, 25))
        font_label = QtGui.QFont()
        font_label.setFamily("Arial")
        font_label.setPointSize(12)
        font_label.setBold(True)
        self.label_user_id.setFont(font_label)
        self.label_user_id.setStyleSheet("color: black; border: none; outline: none;")

        self.input_user_id = QtWidgets.QLineEdit(parent=self.form_widget)
        self.input_user_id.setGeometry(QtCore.QRect(0, 25, 300, 35))
        self.input_user_id.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                color: black;
            }
            
        """)
        self.input_user_id.setPlaceholderText("Enter your User ID or Email")

        # Password
        self.label_password = QtWidgets.QLabel("Password:", parent=self.form_widget)
        self.label_password.setGeometry(QtCore.QRect(0, 70, 100, 25))
        self.label_password.setFont(font_label)
        self.label_password.setStyleSheet("color: black; background: transparent ; border: none; outline: none;")

        self.input_password = QtWidgets.QLineEdit(parent=self.form_widget)
        self.input_password.setGeometry(QtCore.QRect(0, 95, 300, 35))
        self.input_password.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border-radius: 8px;
                padding: 8px;
                font-size: 14px;
                color: black;
            }
            
        """)
        self.input_password.setPlaceholderText("Enter your password")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        # Login Button
        self.btn_login = QtWidgets.QPushButton("LOGIN", parent=self.login_frame)
        self.btn_login.setGeometry(QtCore.QRect(100, 290, 200, 45))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setPointSize(14)
        font_btn.setBold(True)
        self.btn_login.setFont(font_btn)
        self.btn_login.setStyleSheet("""
            QPushButton {
                background-color: #10B981; 
                color: white; 
                border-radius: 10px;
                border: 2px solid #059669;
            }
            QPushButton:hover {
                background-color: #059669;
            }
            QPushButton:pressed {
                background-color: #047857;
            }
        """)



        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons
        self.btn_login.clicked.connect(self.user_login)


        # Connect Enter key to login
        self.input_password.returnPressed.connect(self.user_login)

    def user_login(self):
        user_input = self.input_user_id.text().strip()
        password = self.input_password.text().strip()

        if not user_input or not password:
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter both User ID/Email and password!")
            return

        # Check if user exists in database (by user_id OR email) AND password matches
        db = Database()
        query = "SELECT * FROM users WHERE (user_id = %s OR email = %s) AND password = %s AND status = 'Active'"
        user = db.fetch_one(query, (user_input, user_input, password))

        if user:
            QtWidgets.QMessageBox.information(None, "Success", f"Welcome back, {user['full_name']}!")
            self.open_user_dashboard(user)
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Invalid credentials or user not active!")

    def open_user_dashboard(self, user_data):
        from user_dashboard import UserDashboardWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = UserDashboardWindow()
        self.ui.setupUi(self.window, user_data)
        self.window.show()
        # Close login window
        for widget in QtWidgets.QApplication.topLevelWidgets():
            if widget.objectName() == "UserLoginWindow":
                widget.close()