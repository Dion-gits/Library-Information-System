# admin_login_window.py
from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class AdminLoginWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AdminLoginWindow")
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
        self.label_title = QtWidgets.QLabel("ADMIN LOGIN", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(350, 60, 201, 21))
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

        # Admin Icon
        self.admin_icon = QtWidgets.QLabel("👨‍💼", parent=self.login_frame)
        self.admin_icon.setGeometry(QtCore.QRect(150, 20, 100, 100))
        self.admin_icon.setStyleSheet("""
                    font-size: 80px;
                    border: none;
                    background: transparent;
                """)
        self.admin_icon.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Form Widget
        self.form_widget = QtWidgets.QWidget(parent=self.login_frame)
        self.form_widget.setStyleSheet("""
                    QWidget {
                        background-color: #F3F4F6;  /* same as login_frame */
                        border-radius: 10px;
                    }
                """)
        self.form_widget.setGeometry(QtCore.QRect(50, 130, 300, 150))

        # Username
        self.label_username = QtWidgets.QLabel("Username:", parent=self.form_widget)
        self.label_username.setGeometry(QtCore.QRect(0, 0, 100, 25))
        font_label = QtGui.QFont()
        font_label.setFamily("Arial")
        font_label.setPointSize(12)
        font_label.setBold(True)
        self.label_username.setFont(font_label)
        self.label_username.setStyleSheet("color: black; border: none; outline: none;")

        self.input_username = QtWidgets.QLineEdit(parent=self.form_widget)
        self.input_username.setGeometry(QtCore.QRect(0, 25, 300, 35))
        self.input_username.setStyleSheet("""
                    QLineEdit {
                        background-color: white;
                        border-radius: 8px;
                        padding: 8px;
                        font-size: 14px;
                        color: black;
                    }

                """)
        self.input_username.setPlaceholderText("Enter admin username")

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
        self.input_password.setPlaceholderText("Enter password")
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
                background-color: #7C3AED; 
                color: white; 
                border-radius: 10px;
                border: 2px solid #5B21B6;
            }
            QPushButton:hover {
                background-color: #5B21B6;
            }
            QPushButton:pressed {
                background-color: #4C1D95;
            }
        """)



        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons
        self.btn_login.clicked.connect(self.admin_login)


        # Set default admin credentials
        self.admin_username = "admin"
        self.admin_password = "admin123"

    def admin_login(self):
        username = self.input_username.text().strip()
        password = self.input_password.text().strip()

        if not username or not password:
            QtWidgets.QMessageBox.warning(None, "Error", "Please enter both username and password!")
            return

        # Check admin credentials
        if username == self.admin_username and password == self.admin_password:
            QtWidgets.QMessageBox.information(None, "Success", "Admin login successful!")
            self.open_admin_dashboard()
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Invalid admin credentials!")

    def open_admin_dashboard(self):
        from main_ui import Main_ui
        self.window = QtWidgets.QMainWindow()
        self.ui = Main_ui()
        self.ui.setupUi(self.window)
        self.window.show()
        # Close login window
        for widget in QtWidgets.QApplication.topLevelWidgets():
            if widget.objectName() == "AdminLoginWindow":
                widget.close()