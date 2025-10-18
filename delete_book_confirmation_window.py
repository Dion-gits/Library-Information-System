from PyQt6 import QtCore, QtGui, QtWidgets
from database import Database


class DeleteBookConfirmationWindow:
    def setupUi(self, MainWindow, book_data=None):
        MainWindow.setObjectName("DeleteBookConfirmationWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        MainWindow.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.book_data = book_data

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
        self.label_4 = QtWidgets.QLabel("DELETE BOOK", parent=self.top_frame)
        self.label_4.setGeometry(QtCore.QRect(200, 60, 201, 21))
        font_title = QtGui.QFont()
        font_title.setFamily("Arial Black")
        font_title.setPointSize(18)
        font_title.setBold(True)
        self.label_4.setFont(font_title)
        self.label_4.setStyleSheet("color: white;")

        # --- Main frame ---
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 60, 500, 240))
        self.frame_3.setStyleSheet("background-color: #e2d8f3;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        # Warning icon and message
        self.warning_icon = QtWidgets.QLabel(parent=self.frame_3)
        self.warning_icon.setGeometry(QtCore.QRect(50, 40, 64, 64))
        self.warning_icon.setStyleSheet("font-size: 48px; color: #EF4444;")
        self.warning_icon.setText("⚠️")

        # Warning message
        self.warning_message = QtWidgets.QLabel(parent=self.frame_3)
        self.warning_message.setGeometry(QtCore.QRect(130, 30, 350, 80))
        font_warning = QtGui.QFont()
        font_warning.setPointSize(12)
        font_warning.setBold(True)
        self.warning_message.setFont(font_warning)
        self.warning_message.setStyleSheet("color: black;")
        self.warning_message.setWordWrap(True)

        if book_data:
            self.warning_message.setText(
                f"Are you sure you want to delete book:\n{book_data['title']} ({book_data['isbn']})?\n\nThis action cannot be undone.")
        else:
            self.warning_message.setText("Are you sure you want to delete this book?\n\nThis action cannot be undone.")

        # Book details
        self.book_details = QtWidgets.QLabel(parent=self.frame_3)
        self.book_details.setGeometry(QtCore.QRect(50, 110, 400, 40))
        font_details = QtGui.QFont()
        font_details.setPointSize(10)
        self.book_details.setFont(font_details)
        self.book_details.setStyleSheet("color: #666666;")
        self.book_details.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        if book_data:
            self.book_details.setText(f"ISBN: {book_data.get('isbn', 'N/A')} | Title: {book_data.get('title', 'N/A')}")
        else:
            self.book_details.setText("Book details will be shown here")

        # Buttons
        self.pushButton_cancel = QtWidgets.QPushButton("CANCEL", parent=self.frame_3)
        self.pushButton_cancel.setGeometry(QtCore.QRect(150, 170, 100, 35))
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial")
        font_btn.setBold(True)
        self.pushButton_cancel.setFont(font_btn)
        self.pushButton_cancel.setStyleSheet("background-color: #6B7280; color: white;")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.pushButton_delete = QtWidgets.QPushButton("DELETE", parent=self.frame_3)
        self.pushButton_delete.setGeometry(QtCore.QRect(270, 170, 100, 35))
        self.pushButton_delete.setFont(font_btn)
        self.pushButton_delete.setStyleSheet("background-color: #EF4444; color: white;")
        self.pushButton_delete.setObjectName("pushButton_delete")

        # Sidebar with Go Back button
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.frame_3)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 122, 50))
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

        MainWindow.setCentralWidget(self.centralwidget)

        # Connect buttons
        self.pushButton_cancel.clicked.connect(MainWindow.close)
        self.pushButton_delete.clicked.connect(self.delete_book)

    def delete_book(self):
        """Delete book functionality"""
        if self.book_data:
            try:
                db = Database()
                query = "DELETE FROM books WHERE id = %s"
                result = db.execute_query(query, (self.book_data['id'],))

                if result:
                    QtWidgets.QMessageBox.information(None, "Success",
                                                      f"Book '{self.book_data.get('title', 'Unknown')}' deleted successfully!")
                else:
                    QtWidgets.QMessageBox.warning(None, "Error", "Failed to delete book from database!")
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Error", f"Error deleting book: {str(e)}")
        else:
            QtWidgets.QMessageBox.information(None, "Delete Book",
                                              "Delete functionality will be implemented when system is complete.")

        # Close the confirmation window after deletion attempt
        self.pushButton_cancel.click()