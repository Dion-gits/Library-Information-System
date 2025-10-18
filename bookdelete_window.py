from PyQt6 import QtCore, QtGui, QtWidgets
from delete_book_confirmation_window import DeleteBookConfirmationWindow
from database import Database


class DeleteBookWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DeleteBookWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
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

        # System Name
        self.label_name = QtWidgets.QLabel(parent=self.top_frame)
        self.label_name.setGeometry(QtCore.QRect(70, 30, 141, 91))
        self.label_name.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label_name.setStyleSheet("background-color: transparent;")
        self.label_name.setScaledContents(True)

        # Title
        self.label_title = QtWidgets.QLabel("DELETE BOOK", parent=self.top_frame)
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

        # --- Buttons ---
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)

        self.btn_search = QtWidgets.QPushButton("SEARCH", parent=self.frame_3)
        self.btn_search.setGeometry(QtCore.QRect(670, 20, 81, 25))
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

        # --- Table (EXACTLY like books_window) ---
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

        # Enable row selection
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        # Load books into table
        self.load_books()

        # --- Sidebar buttons ---
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 111, 181))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(6)

        button_style = "background-color: #7C3AED; color: white; font-family: 'Arial Black'; font-weight: bold;"

        self.btn_select = QtWidgets.QPushButton("SELECT BOOK", parent=self.verticalLayoutWidget)
        self.btn_select.setStyleSheet(button_style)
        self.verticalLayout.addWidget(self.btn_select)

        self.btn_back = QtWidgets.QPushButton("Go Back", parent=self.verticalLayoutWidget)
        self.btn_back.setStyleSheet(button_style)
        self.verticalLayout.addWidget(self.btn_back)
        self.btn_back.clicked.connect(MainWindow.close)

        MainWindow.setCentralWidget(self.centralwidget)

        # Connect actions
        self.btn_select.clicked.connect(self.select_book)
        self.table.doubleClicked.connect(self.select_book)

    def load_books(self):
        """Load books from database into table"""
        try:
            query = "SELECT id, isbn, title, author, quantity, available FROM books"
            books = self.db.fetch_all(query)

            self.table.setRowCount(len(books))
            for row, book in enumerate(books):
                # Store book ID in hidden data (we'll use it later)
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(book['isbn']))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(book['title']))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(book['author']))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(book['quantity'])))

                # Determine status based on availability - MODIFIED
                status = "Available" if book['available'] > 0 else "Not Available"
                self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(status))

                # Store the book ID as hidden data in the first column
                self.table.item(row, 0).setData(QtCore.Qt.ItemDataRole.UserRole, book['id'])

        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"Error loading books: {str(e)}")

    def get_selected_book_data(self):
        """Get data of selected book from table"""
        current_row = self.table.currentRow()
        if current_row >= 0:
            try:
                # Get the book ID from hidden data
                book_id = self.table.item(current_row, 0).data(QtCore.Qt.ItemDataRole.UserRole)
                query = "SELECT * FROM books WHERE id = %s"
                book_data = self.db.fetch_all(query, (book_id,))
                if book_data:
                    return book_data[0]
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", f"Error getting book data: {str(e)}")
        return None

    def select_book(self):
        """Open delete confirmation window for selected book"""
        book_data = self.get_selected_book_data()
        if book_data:
            self.delete_confirmation_window = QtWidgets.QMainWindow()
            self.delete_confirmation_ui = DeleteBookConfirmationWindow()
            self.delete_confirmation_ui.setupUi(self.delete_confirmation_window, book_data)
            self.delete_confirmation_window.show()
        else:
            QtWidgets.QMessageBox.warning(None, "Selection Error", "Please select a book to delete!")