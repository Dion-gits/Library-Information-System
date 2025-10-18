from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class Ui_AddBookWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AddBookWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff; color: black;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # --- Top Frame with logo and name ---
        self.top_frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(-10, -40, 821, 101))
        self.top_frame.setStyleSheet("background-color: #E0B3FF;")

        # Logo
        self.logo = QtWidgets.QLabel(parent=self.top_frame)
        self.logo.setGeometry(QtCore.QRect(0, 20, 111, 111))
        self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))  # replace with your path
        self.logo.setScaledContents(True)

        # Name image
        self.label_name = QtWidgets.QLabel(parent=self.top_frame)
        self.label_name.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label_name.setPixmap(QtGui.QPixmap("logofff/name1.png"))  # replace with your path
        self.label_name.setStyleSheet("background: transparent;")
        self.label_name.setScaledContents(True)

        # Title label
        self.label_4 = QtWidgets.QLabel("ADD BOOK", parent=self.top_frame)
        self.label_4.setGeometry(QtCore.QRect(420, 60, 141, 21))
        title_font = QtGui.QFont("Arial Black", 18, QtGui.QFont.Weight.Bold)
        self.label_4.setFont(title_font)
        self.label_4.setStyleSheet("color: white;")  # font color white

        # --- Main frame ---
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 771, 591))
        self.frame_3.setStyleSheet("background-color: #e2d8f3; color: black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # --- Sidebar Buttons ---
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 111, 181))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(6)

        button_style = "background-color: #7C3AED; color: white; font-family: 'Arial Black'; font-weight: bold;"

        self.btn_back = QtWidgets.QPushButton("Go Back", parent=self.verticalLayoutWidget)
        self.btn_back.setStyleSheet(button_style)
        self.verticalLayout.addWidget(self.btn_back)
        self.btn_back.clicked.connect(MainWindow.close)

        # --- Form Fields ---
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(250, 30, 392, 261))
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(12)

        label_font = QtGui.QFont()
        label_font.setPointSize(12)
        label_font.setBold(True)

        def make_lineedit():
            le = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
            le.setStyleSheet("background-color: #FFFFFF; color: black;")
            return le

        # Labels and line edits
        self.label_isbn = QtWidgets.QLabel("ISBN:", parent=self.formLayoutWidget)
        self.label_isbn.setFont(label_font)
        self.lineEdit_isbn = make_lineedit()
        self.formLayout.addRow(self.label_isbn, self.lineEdit_isbn)

        self.label_title = QtWidgets.QLabel("TITLE:", parent=self.formLayoutWidget)
        self.label_title.setFont(label_font)
        self.lineEdit_title = make_lineedit()
        self.formLayout.addRow(self.label_title, self.lineEdit_title)

        self.label_author = QtWidgets.QLabel("AUTHOR/s:", parent=self.formLayoutWidget)
        self.label_author.setFont(label_font)
        self.lineEdit_author = make_lineedit()
        self.formLayout.addRow(self.label_author, self.lineEdit_author)

        self.label_year = QtWidgets.QLabel("YEAR PUBLISHED:", parent=self.formLayoutWidget)
        self.label_year.setFont(label_font)
        self.lineEdit_year = make_lineedit()
        self.formLayout.addRow(self.label_year, self.lineEdit_year)

        self.label_copies = QtWidgets.QLabel("NUMBER OF COPIES:", parent=self.formLayoutWidget)
        self.label_copies.setFont(label_font)
        self.lineEdit_copies = make_lineedit()
        self.formLayout.addRow(self.label_copies, self.lineEdit_copies)

        # Category ComboBox
        self.label_category = QtWidgets.QLabel("CATEGORY:", parent=self.formLayoutWidget)
        self.label_category.setFont(label_font)
        self.combo_category = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.combo_category.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.addRow(self.label_category, self.combo_category)

        # Subcategory ComboBox
        self.label_subcategory = QtWidgets.QLabel("SUBCATEGORY:", parent=self.formLayoutWidget)
        self.label_subcategory.setFont(label_font)
        self.combo_subcategory = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.combo_subcategory.setStyleSheet("background-color: #FFFFFF; color: black;")
        self.formLayout.addRow(self.label_subcategory, self.combo_subcategory)

        # Action Buttons
        self.btn_clear = QtWidgets.QPushButton("CLEAR", parent=self.frame_3)
        self.btn_clear.setGeometry(QtCore.QRect(350, 330, 75, 24))
        self.btn_clear.setStyleSheet("background-color: red; color: white; font-weight: bold;")

        self.btn_add_form = QtWidgets.QPushButton("ADD", parent=self.frame_3)
        self.btn_add_form.setGeometry(QtCore.QRect(450, 330, 75, 24))
        self.btn_add_form.setStyleSheet("background-color: green; color: white; font-weight: bold;")

        # Dewey Categories
        self.dewey_categories = {
            "000 – General Works": ["000–099 Generalities", "010–019 Bibliographies",
                                    "020–029 Library & information sciences"],
            "100 – Philosophy & Psychology": ["110 Metaphysics", "120 Epistemology", "150 Psychology"],
            "200 – Religion": ["220 Bible", "230 Christianity", "290 Other religions"],
            "300 – Social Sciences": ["320 Political science", "330 Economics", "370 Education"],
            "400 – Language": ["410 Linguistics", "420 English", "490 Other languages"],
            "500 – Science": ["510 Mathematics", "520 Astronomy", "540 Chemistry", "570 Biology"],
            "600 – Technology": ["610 Medicine", "620 Engineering", "640 Home economics"],
            "700 – Arts & Recreation": ["730 Sculpture", "740 Drawing", "790 Sports & recreation"],
            "800 – Literature": ["810 American literature", "820 English literature", "890 Other literatures"],
            "900 – History & Geography": ["910 Geography", "930 History of ancient world",
                                          "970 History of North America"]
        }

        self.combo_category.addItems(self.dewey_categories.keys())
        self.combo_category.currentTextChanged.connect(self.update_subcategories)
        self.update_subcategories(self.combo_category.currentText())

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to functions
        self.btn_clear.clicked.connect(self.clear_form)
        self.btn_add_form.clicked.connect(self.add_book_to_database)

    def update_subcategories(self, category):
        """Update subcategory combo box based on selected category."""
        self.combo_subcategory.clear()
        subcats = self.dewey_categories.get(category, [])
        self.combo_subcategory.addItems(subcats)

    def clear_form(self):
        """Clear all form fields"""
        self.lineEdit_isbn.clear()
        self.lineEdit_title.clear()
        self.lineEdit_author.clear()
        self.lineEdit_year.clear()
        self.lineEdit_copies.clear()
        self.combo_category.setCurrentIndex(0)
        self.update_subcategories(self.combo_category.currentText())

    def add_book_to_database(self):
        """Add book to MySQL database"""
        try:
            # Get data from form
            isbn = self.lineEdit_isbn.text().strip()
            title = self.lineEdit_title.text().strip()
            author = self.lineEdit_author.text().strip()
            year = self.lineEdit_year.text().strip()
            copies = self.lineEdit_copies.text().strip()
            category = self.combo_category.currentText()
            subcategory = self.combo_subcategory.currentText()

            # Validate required fields
            if not all([isbn, title, author, year, copies]):
                QtWidgets.QMessageBox.warning(None, "Error", "Please fill in all required fields!")
                return

            # Validate year and copies are numbers
            try:
                year_int = int(year)
                copies_int = int(copies)
                if copies_int <= 0:
                    QtWidgets.QMessageBox.warning(None, "Error", "Number of copies must be greater than 0!")
                    return
            except ValueError:
                QtWidgets.QMessageBox.warning(None, "Error", "Year and Copies must be numbers!")
                return

            # Connect to database
            db = Database()

            # Check if ISBN already exists
            check_query = "SELECT id FROM books WHERE isbn = %s"
            existing_book = db.fetch_all(check_query, (isbn,))

            if existing_book:
                QtWidgets.QMessageBox.warning(None, "Error", f"Book with ISBN {isbn} already exists!")
                return

            # Insert new book - MODIFIED: Set available = quantity
            insert_query = """
                INSERT INTO books (isbn, title, author, publication_year, quantity, available, genre)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            # Use category as genre for now, you can modify this to include subcategory if needed
            params = (isbn, title, author, year_int, copies_int, copies_int, category)

            result = db.execute_query(insert_query, params)

            if result:
                QtWidgets.QMessageBox.information(None, "Success",
                                                  f"Book '{title}' added successfully!\n"
                                                  f"ISBN: {isbn}\n"
                                                  f"Copies: {copies}\n"
                                                  f"Status: Available")
                self.clear_form()
            else:
                QtWidgets.QMessageBox.warning(None, "Error", "Failed to add book to database!")

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error adding book: {str(e)}")