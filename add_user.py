from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database

class AddUserWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AddUserWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- Top frame ---
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

        # Title in top frame
        self.label_4 = QtWidgets.QLabel("ADD USER", parent=self.top_frame)
        self.label_4.setGeometry(QtCore.QRect(380, 60, 201, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_4.setFont(font_title)
        self.label_4.setStyleSheet("color: white;")

        # --- Main frame ---
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.frame_3.setStyleSheet("background-color: #e2d8f3;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        # Form layout widget
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(240, 60, 392, 401))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setObjectName("formLayout")

        # User ID Field
        self.label_user_id = QtWidgets.QLabel("User ID:", parent=self.formLayoutWidget)
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)
        self.label_user_id.setFont(font_label)
        self.label_user_id.setStyleSheet("color: black;")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_user_id)

        self.lineEdit_user_id = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)
        self.lineEdit_user_id.setSizePolicy(sizePolicy)
        self.lineEdit_user_id.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_user_id)

        # Full Name Field
        self.label_full_name = QtWidgets.QLabel("Full Name:", parent=self.formLayoutWidget)
        self.label_full_name.setFont(font_label)
        self.label_full_name.setStyleSheet("color: black;")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_full_name)

        self.lineEdit_full_name = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_full_name.setSizePolicy(sizePolicy)
        self.lineEdit_full_name.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_full_name)

        # Age Field
        self.label_age = QtWidgets.QLabel("Age:", parent=self.formLayoutWidget)
        self.label_age.setFont(font_label)
        self.label_age.setStyleSheet("color: black;")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_age)

        self.lineEdit_age = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_age.setSizePolicy(sizePolicy)
        self.lineEdit_age.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_age)

        # Password Field
        self.label_password = QtWidgets.QLabel("Password:", parent=self.formLayoutWidget)
        self.label_password.setFont(font_label)
        self.label_password.setStyleSheet("color: black;")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_password)

        self.lineEdit_password = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_password)

        # Email Field
        self.label_email = QtWidgets.QLabel("Email:", parent=self.formLayoutWidget)
        self.label_email.setFont(font_label)
        self.label_email.setStyleSheet("color: black;")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_email)

        self.lineEdit_email = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_email.setSizePolicy(sizePolicy)
        self.lineEdit_email.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_email)

        # Contact No. Field
        self.label_contact = QtWidgets.QLabel("Contact No.:", parent=self.formLayoutWidget)
        self.label_contact.setFont(font_label)
        self.label_contact.setStyleSheet("color: black;")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_contact)

        self.lineEdit_contact = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_contact.setSizePolicy(sizePolicy)
        self.lineEdit_contact.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_contact)

        # Address Field
        self.label_address = QtWidgets.QLabel("Address:", parent=self.formLayoutWidget)
        self.label_address.setFont(font_label)
        self.label_address.setStyleSheet("color: black;")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_address)

        self.lineEdit_address = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_address.setSizePolicy(sizePolicy)
        self.lineEdit_address.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_address)

        # Status Field
        self.label_status = QtWidgets.QLabel("Status:", parent=self.formLayoutWidget)
        self.label_status.setFont(font_label)
        self.label_status.setStyleSheet("color: black;")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_status)

        self.comboBox_status = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.comboBox_status.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.comboBox_status.addItems(["Active", "Not Active"])
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.comboBox_status)

        # Fees Field
        self.label_fees = QtWidgets.QLabel("Fees:", parent=self.formLayoutWidget)
        self.label_fees.setFont(font_label)
        self.label_fees.setStyleSheet("color: black;")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_fees)

        self.lineEdit_fees = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.lineEdit_fees.setSizePolicy(sizePolicy)
        self.lineEdit_fees.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.lineEdit_fees.setText("0.00")
        self.lineEdit_fees.setReadOnly(True)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_fees)

        # Buttons
        self.pushButton_clear = QtWidgets.QPushButton("CLEAR", parent=self.frame_3)
        self.pushButton_clear.setGeometry(QtCore.QRect(350, 480, 75, 24))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial")
        font_btn.setBold(True)
        self.pushButton_clear.setFont(font_btn)
        self.pushButton_clear.setStyleSheet("background-color: red; color: white")
        self.pushButton_clear.setObjectName("pushButton_clear")

        self.pushButton_add = QtWidgets.QPushButton("ADD", parent=self.frame_3)
        self.pushButton_add.setGeometry(QtCore.QRect(450, 480, 75, 24))
        self.pushButton_add.setFont(font_btn)
        self.pushButton_add.setStyleSheet("background-color: green; color: white")
        self.pushButton_add.setObjectName("pushButton_add")

        # Sidebar with Go Back button
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 122, 181))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.pushButton_go_back = QtWidgets.QPushButton("Go Back", parent=self.verticalLayoutWidget_2)
        self.pushButton_go_back.setFont(font_btn)
        self.pushButton_go_back.setStyleSheet("background-color: #7C3AED; color: white")
        self.verticalLayout_2.addWidget(self.pushButton_go_back)
        self.pushButton_go_back.clicked.connect(MainWindow.close)

        # Form title
        self.label_title = QtWidgets.QLabel("ADD USER FORM", parent=self.frame_3)
        self.label_title.setGeometry(QtCore.QRect(370, 20, 171, 21))
        font_form_title = QtGui.QFont()
        font_form_title.setFamily("Arial Black")
        font_form_title.setPointSize(18)
        font_form_title.setBold(True)
        self.label_title.setFont(font_form_title)
        self.label_title.setStyleSheet("color: black;")

        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons
        self.pushButton_clear.clicked.connect(self.clear_form)
        self.pushButton_add.clicked.connect(self.add_user_to_database)

    def add_user_to_database(self):
        """Add user to MySQL database"""
        try:
            # Get data from form
            user_id = self.lineEdit_user_id.text().strip()
            full_name = self.lineEdit_full_name.text().strip()
            age = self.lineEdit_age.text().strip()
            password = self.lineEdit_password.text().strip()
            email = self.lineEdit_email.text().strip()
            contact = self.lineEdit_contact.text().strip()
            address = self.lineEdit_address.text().strip()
            status = self.comboBox_status.currentText()
            fees = 0.00

            # Validate required fields
            if not all([user_id, full_name, age, password, email, contact, address]):
                QtWidgets.QMessageBox.warning(None, "Error", "Please fill in all required fields!")
                return

            # Validate age
            try:
                age_int = int(age)
                if age_int <= 0:
                    QtWidgets.QMessageBox.warning(None, "Error", "Age must be greater than 0!")
                    return
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Error", "Age must be a number!")
                return

            # Connect to database
            db = Database()

            # Check if user ID already exists
            check_query = "SELECT id FROM users WHERE user_id = %s"
            existing_user = db.fetch_all(check_query, (user_id,))

            if existing_user:
                QtWidgets.QMessageBox.warning(None, "Error", f"User with ID {user_id} already exists!")
                return

            # Insert new user
            insert_query = """
                INSERT INTO users (user_id, full_name, age, password, email, contact, address, status, fees)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (user_id, full_name, age_int, password, email, contact, address, status, fees)

            result = db.execute_query(insert_query, params)

            if result:
                QtWidgets.QMessageBox.information(None, "Success",
                                                  f"User '{full_name}' added successfully!\n"
                                                  f"User ID: {user_id}")
                self.clear_form()
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Failed to add user to database!")

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error adding user: {str(e)}")

    def clear_form(self):
        """Clear the form"""
        self.lineEdit_user_id.clear()
        self.lineEdit_full_name.clear()
        self.lineEdit_age.clear()
        self.lineEdit_password.clear()
        self.lineEdit_email.clear()
        self.lineEdit_contact.clear()
        self.lineEdit_address.clear()
        self.comboBox_status.setCurrentIndex(0)
        self.lineEdit_fees.setText("0.00")