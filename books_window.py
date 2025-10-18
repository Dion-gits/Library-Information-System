from PyQt6 import QtCore, QtGui, QtWidgets
from addbook_window import Ui_AddBookWindow as AddBookWindow
from updatebook_window import UpdateBookWindow
from bookdelete_window import DeleteBookWindow
from database import Database
from PyQt6.QtCore import QTimer

class BooksWindow:
    # def setupUi(self, MainWindow):
    #     print("UserWindow setupUi starting")
    #     # return immediately to skip loading code
    #     return
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("BooksWindow")
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
        self.label_title = QtWidgets.QLabel("All BOOKS", parent=self.top_frame)
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
        self.lineEdit.setPlaceholderText("Search book...")

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
        self.comboBox_2.addItems(["Default", "A-Z", "Z-A", "Year Published", "Date Added"])


        # --- Table ---
        self.table = QtWidgets.QTableWidget(parent=self.frame_3)
        self.table.setGeometry(QtCore.QRect(150, 60, 611, 501))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ISBN", "Title", "Author", "Copies", "Status"])
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

        # QtCore.QTimer.singleShot(0, self.load_books_from_database)

        # Load books from database
        self.load_books_from_database()

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
        self.btn_search.clicked.connect(self.search_action)
        self.btn_sort.clicked.connect(self.sort_action)


    def load_books_from_database(self):
        """Load books from MySQL database into table"""
        try:
            query = "SELECT isbn, title, author, quantity, available FROM books ORDER BY title"
            books = self.db.fetch_all(query)

            self.table.setRowCount(len(books))
            for row, book in enumerate(books):
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(book['isbn']))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(book['title']))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(book['author']))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(book['quantity'])))

                # Determine status based on availability - MODIFIED
                status = "Available" if book['available'] > 0 else "Not Available"
                self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(status))

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error loading books from database: {str(e)}")

    # --- Functions ---
    def open_add(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AddBookWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.destroyed.connect(self.load_books_from_database)

    def open_update(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UpdateBookWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.destroyed.connect(self.load_books_from_database)

    def open_delete(self):
        self.delete_window = QtWidgets.QMainWindow()
        self.ui_delete = DeleteBookWindow()
        self.ui_delete.setupUi(self.delete_window)
        self.delete_window.show()
        self.delete_window.destroyed.connect(self.load_books_from_database)

    def search_action(self):
        keyword = self.lineEdit.text().strip()
        if keyword:
            try:
                query = """
                    SELECT isbn, title, author, quantity, available
                    FROM books
                    WHERE isbn LIKE %s OR title LIKE %s OR author LIKE %s OR genre LIKE %s
                    ORDER BY title
                """
                search_term = f"%{keyword}%"
                books = self.db.fetch_all(query, (search_term, search_term, search_term, search_term))

                self.table.setRowCount(len(books))
                for row, book in enumerate(books):
                    self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(book['isbn']))
                    self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(book['title']))
                    self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(book['author']))
                    self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(book['quantity'])))
                    # MODIFIED: Status based on availability > 0
                    status = "Available" if book['available'] > 0 else "Not Available"
                    self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(status))

            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", f"Error searching books: {str(e)}")
        else:
            self.load_books_from_database()

    def sort_action(self):
        """Sort books based on the selected option in the sort combo box."""
        sort_by = self.comboBox_2.currentText().strip()

        try:
            # Determine SQL ORDER BY based on dropdown selection
            if sort_by == "A-Z":
                order_by = "title ASC"
            elif sort_by == "Z-A":
                order_by = "title DESC"
            elif sort_by == "Year Published":
                # Adjust column name to your DB’s actual year field
                order_by = "publication_year DESC"
            elif sort_by == "Date Added":
                # Adjust to your DB column for date added
                order_by = "created_at DESC"
            else:  # Default
                order_by = "title ASC"

            # Query and fetch data
            query = f"SELECT isbn, title, author, quantity, available FROM books ORDER BY {order_by}"
            books = self.db.fetch_all(query)

            # Refresh table content
            self.table.setRowCount(len(books))
            for row, book in enumerate(books):
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(book["isbn"]))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(book["title"]))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(book["author"]))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(book["quantity"])))

                # Determine status based on availability
                status = "Available" if book["available"] > 0 else "Not Available"
                self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(status))

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error sorting books: {str(e)}")
