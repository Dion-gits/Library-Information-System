# user_catalog_window.py
from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class UserCatalogWindow:
    def setupUi(self, MainWindow, user_data):
        MainWindow.setObjectName("UserCatalogWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.user_data = user_data
        self.db = Database()

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
        self.label_title = QtWidgets.QLabel("BOOK CATALOG", parent=self.top_frame)
        self.label_title.setGeometry(QtCore.QRect(320, 60, 251, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(16)
        font_title.setBold(True)
        self.label_title.setFont(font_title)
        self.label_title.setStyleSheet("color: white;")

        # Back Button
        self.btn_back = QtWidgets.QPushButton("← Back", parent=self.top_frame)
        self.btn_back.setGeometry(QtCore.QRect(680, 60, 80, 25))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)
        self.btn_back.setFont(font_btn)
        self.btn_back.setStyleSheet("background-color: #6B7280; color: white; border-radius: 5px;")

        # Main Frame
        self.main_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.main_frame.setStyleSheet("background-color: #e2d8f3;")
        self.main_frame.setObjectName("main_frame")

        # Content Label
        self.label_content = QtWidgets.QLabel("Book Catalog - Under Development", parent=self.main_frame)
        self.label_content.setGeometry(QtCore.QRect(200, 250, 400, 50))
        self.label_content.setStyleSheet("color: black; font-size: 20px; font-weight: bold;")
        self.label_content.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons
        self.btn_back.clicked.connect(MainWindow.close)