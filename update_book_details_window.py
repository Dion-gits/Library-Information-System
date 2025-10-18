from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class UpdateBookDetailsWindow:
    def setupUi(self, MainWindow, book_data=None):
        MainWindow.setObjectName("UpdateBookDetailsWindow")
        MainWindow.resize(766, 637)
        MainWindow.setMinimumSize(QtCore.QSize(766, 637))
        MainWindow.setMaximumSize(QtCore.QSize(766, 637))
        MainWindow.setStyleSheet("background-color: #ffffff;")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_window = MainWindow
        self.book_data = book_data
        self.db = Database()

        # --- Top frame (MATCHING OTHER WINDOWS) ---
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
        self.label_title = QtWidgets.QLabel("UPDATE BOOK DETAILS", parent=self.top_frame)
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

        # Fields
        self.label_book_id = QtWidgets.QLabel("Book ID:")
        self.label_book_id.setStyleSheet(label_style)
        self.lineEdit_book_id = QtWidgets.QLineEdit()
        self.lineEdit_book_id.setReadOnly(True)
        self.lineEdit_book_id.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_book_id, self.lineEdit_book_id)

        self.label_isbn = QtWidgets.QLabel("ISBN:")
        self.label_isbn.setStyleSheet(label_style)
        self.lineEdit_isbn = QtWidgets.QLineEdit()
        self.lineEdit_isbn.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_isbn, self.lineEdit_isbn)

        self.label_title_field = QtWidgets.QLabel("Title:")
        self.label_title_field.setStyleSheet(label_style)
        self.lineEdit_title = QtWidgets.QLineEdit()
        self.lineEdit_title.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_title_field, self.lineEdit_title)

        self.label_author = QtWidgets.QLabel("Author:")
        self.label_author.setStyleSheet(label_style)
        self.lineEdit_author = QtWidgets.QLineEdit()
        self.lineEdit_author.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_author, self.lineEdit_author)

        self.label_year = QtWidgets.QLabel("Year Published:")
        self.label_year.setStyleSheet(label_style)
        self.lineEdit_year = QtWidgets.QLineEdit()
        self.lineEdit_year.setPlaceholderText("e.g., 2024")
        self.lineEdit_year.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_year, self.lineEdit_year)

        self.label_quantity = QtWidgets.QLabel("Quantity:")
        self.label_quantity.setStyleSheet(label_style)
        self.lineEdit_quantity = QtWidgets.QLineEdit()
        self.lineEdit_quantity.setPlaceholderText("e.g., 5")
        self.lineEdit_quantity.setStyleSheet(field_style)
        self.formLayout.addRow(self.label_quantity, self.lineEdit_quantity)

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

        # ✅ Create and style buttons
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
        if book_data:
            self.prefill_form(book_data)
        self.pushButton_clear.clicked.connect(self.clear_form)
        self.pushButton_update.clicked.connect(self.update_book)
        self.pushButton_go_back.clicked.connect(MainWindow.close)

        self.set_tab_order()

    def set_tab_order(self):
        """Set proper tab order for form navigation"""
        QtWidgets.QWidget.setTabOrder(self.lineEdit_isbn, self.lineEdit_title)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_title, self.lineEdit_author)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_author, self.lineEdit_year)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_year, self.lineEdit_quantity)
        QtWidgets.QWidget.setTabOrder(self.lineEdit_quantity, self.pushButton_update)
        QtWidgets.QWidget.setTabOrder(self.pushButton_update, self.pushButton_clear)
        QtWidgets.QWidget.setTabOrder(self.pushButton_clear, self.pushButton_go_back)

    def prefill_form(self, book_data):
        """Pre-fill the form with the selected book's data"""
        try:
            if book_data:
                self.lineEdit_book_id.setText(str(book_data.get('id', '')))
                self.lineEdit_isbn.setText(book_data.get('isbn', ''))
                self.lineEdit_title.setText(book_data.get('title', ''))
                self.lineEdit_author.setText(book_data.get('author', ''))
                self.lineEdit_year.setText(str(book_data.get('publication_year', '')))
                self.lineEdit_quantity.setText(str(book_data.get('quantity', '')))
        except Exception as e:
            self.show_error_message(f"Error loading book data: {str(e)}")

    def clear_form(self):
        """Clear all form fields except Book ID"""
        self.lineEdit_isbn.clear()
        self.lineEdit_title.clear()
        self.lineEdit_author.clear()
        self.lineEdit_year.clear()
        self.lineEdit_quantity.clear()

    def validate_fields(self):
        """Validate all form fields before updating"""
        isbn = self.lineEdit_isbn.text().strip()
        title = self.lineEdit_title.text().strip()
        author = self.lineEdit_author.text().strip()
        year = self.lineEdit_year.text().strip()
        quantity = self.lineEdit_quantity.text().strip()

        # Check required fields
        if not all([isbn, title, author, year, quantity]):
            return False, "Please fill in all required fields!"

        # Validate ISBN (basic validation)
        if len(isbn) < 10:
            return False, "ISBN must be at least 10 characters long!"

        # Validate year
        try:
            year_int = int(year)
            current_year = QtCore.QDate.currentDate().year()
            if year_int < 1000 or year_int > current_year:
                return False, f"Year must be between 1000 and {current_year}"
        except ValueError:
            return False, "Year must be a valid number!"

        # Validate quantity
        try:
            quantity_int = int(quantity)
            if quantity_int < 0:
                return False, "Quantity cannot be negative!"
            if quantity_int > 1000:
                return False, "Quantity seems too high. Please verify!"
        except ValueError:
            return False, "Quantity must be a valid number!"

        return True, "All fields are valid"

    def update_book(self):
        """Update book in database"""
        try:
            # Validate fields first
            is_valid, error_message = self.validate_fields()
            if not is_valid:
                self.show_error_message(error_message)
                return

            # Get form data
            book_id = self.lineEdit_book_id.text().strip()
            isbn = self.lineEdit_isbn.text().strip()
            title = self.lineEdit_title.text().strip()
            author = self.lineEdit_author.text().strip()
            year = self.lineEdit_year.text().strip()
            quantity = self.lineEdit_quantity.text().strip()

            # Check if book ID exists
            if not book_id:
                self.show_error_message("No book selected for update!")
                return

            # Update book in database
            query = """
                UPDATE books 
                SET isbn = %s, title = %s, author = %s, 
                    publication_year = %s, quantity = %s 
                WHERE id = %s
            """
            params = (isbn, title, author, int(year), int(quantity), book_id)

            # Show confirmation dialog
            reply = QtWidgets.QMessageBox.question(
                self.main_window,
                "Confirm Update",
                f"Are you sure you want to update '{title}'?",
                QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
                QtWidgets.QMessageBox.StandardButton.No
            )

            if reply == QtWidgets.QMessageBox.StandardButton.Yes:
                result = self.db.execute_query(query, params)

                if result:
                    self.show_success_message(f"Book '{title}' updated successfully!")
                    # Don't clear the form, keep the data for further editing
                else:
                    self.show_error_message("Failed to update book in database. Please try again.")

        except Exception as e:
            self.show_error_message(f"Error updating book: {str(e)}")

    def show_success_message(self, message):
        """Show success message"""
        msg = QtWidgets.QMessageBox(self.main_window)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText(message)
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        # Style the message box
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QMessageBox QLabel {
                color: #059669;
                font-size: 12px;
            }
        """)

        msg.exec()

    def show_error_message(self, message):
        """Show error message"""
        msg = QtWidgets.QMessageBox(self.main_window)
        msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

        # Style the message box
        msg.setStyleSheet("""
            QMessageBox {
                background-color: white;
            }
            QMessageBox QLabel {
                color: #dc2626;
                font-size: 12px;
            }
        """)

        msg.exec()