from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QBarSeries, QBarSet, QValueAxis, QBarCategoryAxis
from database import Database
import pandas as pd
import os
from datetime import datetime

# Button Styles
primary_button_style = """
    QPushButton {
        background-color: #7C3AED;
        color: white;
        border: 2px solid #5B21B6;
        border-radius: 5px;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #5B21B6;
        border-color: #4C1D95;
    }
    QPushButton:pressed {
        background-color: #4C1D95;
        border-color: #3C1A70;
    }
"""

success_button_style = """
    QPushButton {
        background-color: #10B981;
        color: white;
        border: 2px solid #059669;
        border-radius: 5px;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #059669;
    }
    QPushButton:pressed {
        background-color: #047857;
    }
"""

danger_button_style = """
    QPushButton {
        background-color: #EF4444;
        color: white;
        border: 2px solid #DC2626;
        border-radius: 5px;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #DC2626;
    }
    QPushButton:pressed {
        background-color: #B91C1C;
    }
"""

secondary_button_style = """
    QPushButton {
        background-color: #E0B3FF;
        color: #4C1D95;
        border: 2px solid #C084FC;
        border-radius: 5px;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #C084FC;
        color: white;
    }
    QPushButton:pressed {
        background-color: #A855F7;
        border-color: #9333EA;
    }
"""

warning_button_style = """
    QPushButton {
        background-color: #F59E0B;
        color: white;
        border: 2px solid #D97706;
        border-radius: 5px;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #D97706;
    }
    QPushButton:pressed {
        background-color: #B45309;
    }
"""

neutral_button_style = """
    QPushButton {
        background-color: #6B7280;
        color: white;
        border: 2px solid #4B5563;
        border-radius: 5px;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #4B5563;
    }
    QPushButton:pressed {
        background-color: #374151;
    }
"""


class ReportsWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ReportsWindow")
        MainWindow.resize(800, 700)
        MainWindow.setStyleSheet("background-color: #ffffff;")

        # Create central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Create main vertical layout
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # --- Top frame ---
        self.top_frame = QtWidgets.QFrame()
        self.top_frame.setFixedHeight(100)
        self.top_frame.setStyleSheet("background-color: #E0B3FF;")

        top_layout = QtWidgets.QHBoxLayout(self.top_frame)
        top_layout.setContentsMargins(20, 10, 20, 10)

        # Logo
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("logofff/logo1.png"))
        self.logo.setScaledContents(True)
        self.logo.setFixedSize(80, 80)
        self.logo.setStyleSheet("background: transparent;")

        # Name label
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(QtGui.QPixmap("logofff/name1.png"))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setScaledContents(True)
        self.label.setFixedSize(120, 60)

        # Title
        self.label_title = QtWidgets.QLabel("REPORTS")
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: white;")

        # Add widgets to top layout
        top_layout.addWidget(self.logo)
        top_layout.addWidget(self.label)
        top_layout.addStretch()
        top_layout.addWidget(self.label_title)
        top_layout.addStretch()

        # --- Scroll Area for Main Content ---
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("""
            QScrollArea { 
                border: none; 
                background-color: #ffffff; 
            }
            QScrollBar:vertical {
                background: #f1f1f1;
                width: 10px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #c1c1c1;
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: #a8a8a8;
            }
        """)

        # Create scroll widget
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setStyleSheet("background-color: #e2d8f3;")

        # Main layout for scroll widget
        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.scrollLayout.setContentsMargins(20, 20, 20, 20)
        self.scrollLayout.setSpacing(15)

        # --- Data Cards Section ---
        self.create_data_cards()

        # Add data cards in a horizontal layout
        cards_layout = QtWidgets.QHBoxLayout()
        cards_layout.addWidget(self.card_total_books)
        cards_layout.addWidget(self.card_borrowed_books)
        cards_layout.addWidget(self.card_overdue_books)
        cards_layout.addWidget(self.card_returned_books)
        cards_layout.addWidget(self.card_total_transactions)
        cards_layout.addStretch()
        self.scrollLayout.addLayout(cards_layout)

        # --- Report Controls Section ---
        self.create_report_controls()

        # --- Report Display Area ---
        self.textEdit_report = QtWidgets.QTextEdit()
        self.textEdit_report.setMinimumHeight(200)
        self.textEdit_report.setStyleSheet("""
            QTextEdit { 
                border: 1px solid #e2e8f0; 
                background: white; 
                border-radius: 6px; 
                font-size: 12px; 
                color: black; 
                padding: 10px;
            }
        """)
        self.textEdit_report.setPlaceholderText("Generated report will appear here...")
        self.scrollLayout.addWidget(self.textEdit_report)

        # --- Action Buttons ---
        action_buttons_layout = QtWidgets.QHBoxLayout()

        self.btn_back = QtWidgets.QPushButton("Go Back")
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)
        self.btn_back.setFont(font_btn)
        self.btn_back.setFixedHeight(35)
        self.btn_back.setStyleSheet(secondary_button_style)
        self.btn_back.clicked.connect(MainWindow.close)

        action_buttons_layout.addWidget(self.btn_back)
        action_buttons_layout.addStretch()

        self.scrollLayout.addLayout(action_buttons_layout)

        # --- Graph Area ---
        self.create_graphs()

        # Add graphs to scroll layout
        self.scrollLayout.addWidget(self.label_activity_graph)
        self.scrollLayout.addWidget(self.chart_view_activity)
        self.scrollLayout.addWidget(self.label_users_graph)
        self.scrollLayout.addWidget(self.chart_view_users)

        # Set scroll area widget
        self.scrollArea.setWidget(self.scrollWidget)

        # Add everything to main layout
        main_layout.addWidget(self.top_frame)
        main_layout.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        # --- Connect actions ---
        self.btn_generate.clicked.connect(self.generate_report)
        self.btn_export_pdf.clicked.connect(self.export_pdf)
        self.btn_export_excel.clicked.connect(self.export_excel)
        self.btn_import_excel.clicked.connect(self.import_excel)

        self.create_test_data_if_empty()

        # Initialize data cards with real data
        self.update_data_cards()
        # Initialize graphs
        self.update_graphs()

    def create_data_cards(self):
        # Card 1: Total Books
        self.card_total_books = self.create_card("TOTAL BOOKS", "0", "#7C3AED")
        # Card 2: Borrowed Books
        self.card_borrowed_books = self.create_card("BORROWED BOOKS", "0", "#3B82F6")
        # Card 3: Overdue Books
        self.card_overdue_books = self.create_card("OVERDUE BOOKS", "0", "#EF4444")
        # Card 4: Returned Books
        self.card_returned_books = self.create_card("RETURNED BOOKS", "0", "#10B981")
        # Card 5: Total Transactions
        self.card_total_transactions = self.create_card("TOTAL TRANSACTIONS", "0", "#F59E0B")

    def create_card(self, title, value, color):
        card = QtWidgets.QFrame()
        card.setFixedSize(140, 90)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {color};
                border-radius: 8px;
                border: 2px solid {color};
            }}
        """)

        layout = QtWidgets.QVBoxLayout(card)
        layout.setContentsMargins(10, 5, 10, 5)

        title_label = QtWidgets.QLabel(title)
        title_label.setStyleSheet("color: white; font-weight: bold; font-size: 10px;")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        value_label = QtWidgets.QLabel(value)
        value_label.setStyleSheet("color: white; font-weight: bold; font-size: 24px;")
        value_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        layout.addWidget(title_label)
        layout.addWidget(value_label)

        # Store reference to value label for updating
        if title == "TOTAL BOOKS":
            self.label_total_books_value = value_label
        elif title == "BORROWED BOOKS":
            self.label_borrowed_books_value = value_label
        elif title == "OVERDUE BOOKS":
            self.label_overdue_books_value = value_label
        elif title == "RETURNED BOOKS":
            self.label_returned_books_value = value_label
        elif title == "TOTAL TRANSACTIONS":
            self.label_total_transactions_value = value_label

        return card

    def create_report_controls(self):
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)

        # Report Type
        report_type_layout = QtWidgets.QHBoxLayout()
        self.label_report_type = QtWidgets.QLabel("Report Type:")
        self.label_report_type.setFont(font_label)
        self.label_report_type.setStyleSheet("color: black;")
        self.label_report_type.setFixedWidth(120)

        self.comboBox_report_type = QtWidgets.QComboBox()
        self.comboBox_report_type.setFixedHeight(30)
        self.comboBox_report_type.setStyleSheet("background-color: white; color: black;")
        self.comboBox_report_type.addItems([
            "Summary Report",
            "Books Report",
            "Users Report",
            "Borrowing Report",
            "Overdue Books Report",
            "Popular Books Report",
            "Folder Report"
        ])

        report_type_layout.addWidget(self.label_report_type)
        report_type_layout.addWidget(self.comboBox_report_type)
        report_type_layout.addStretch()
        self.scrollLayout.addLayout(report_type_layout)

        # Date Range
        date_layout = QtWidgets.QHBoxLayout()

        self.label_date_from = QtWidgets.QLabel("From:")
        self.label_date_from.setFont(font_label)
        self.label_date_from.setStyleSheet("color: black;")
        self.label_date_from.setFixedWidth(40)

        self.dateEdit_from = QtWidgets.QDateEdit()
        self.dateEdit_from.setFixedHeight(30)
        self.dateEdit_from.setStyleSheet("background-color: white; color: black;")
        self.dateEdit_from.setDate(QtCore.QDate.currentDate().addMonths(-1))

        self.label_date_to = QtWidgets.QLabel("To:")
        self.label_date_to.setFont(font_label)
        self.label_date_to.setStyleSheet("color: black;")
        self.label_date_to.setFixedWidth(20)

        self.dateEdit_to = QtWidgets.QDateEdit()
        self.dateEdit_to.setFixedHeight(30)
        self.dateEdit_to.setStyleSheet("background-color: white; color: black;")
        self.dateEdit_to.setDate(QtCore.QDate.currentDate())

        date_layout.addWidget(self.label_date_from)
        date_layout.addWidget(self.dateEdit_from)
        date_layout.addWidget(self.label_date_to)
        date_layout.addWidget(self.dateEdit_to)
        date_layout.addStretch()
        self.scrollLayout.addLayout(date_layout)

        # Graph Period
        graph_period_layout = QtWidgets.QHBoxLayout()
        self.label_graph_period = QtWidgets.QLabel("Graph Period:")
        self.label_graph_period.setFont(font_label)
        self.label_graph_period.setStyleSheet("color: black;")
        self.label_graph_period.setFixedWidth(120)

        self.comboBox_graph_period = QtWidgets.QComboBox()
        self.comboBox_graph_period.setFixedHeight(30)
        self.comboBox_graph_period.setStyleSheet("background-color: white; color: black;")
        self.comboBox_graph_period.addItems(["Daily", "Monthly", "Yearly"])
        self.comboBox_graph_period.currentTextChanged.connect(self.update_graphs)

        graph_period_layout.addWidget(self.label_graph_period)
        graph_period_layout.addWidget(self.comboBox_graph_period)
        graph_period_layout.addStretch()
        self.scrollLayout.addLayout(graph_period_layout)

        # --- Action Buttons Section ---
        buttons_main_layout = QtWidgets.QHBoxLayout()

        # Left side - Generate Report button
        self.btn_generate = QtWidgets.QPushButton("GENERATE REPORT")
        font_btn = QtGui.QFont()
        font_btn.setFamily("Arial Black")
        font_btn.setBold(True)
        self.btn_generate.setFont(font_btn)
        self.btn_generate.setFixedHeight(35)
        self.btn_generate.setStyleSheet(primary_button_style)
        self.btn_generate.clicked.connect(self.generate_report)

        buttons_main_layout.addWidget(self.btn_generate)
        buttons_main_layout.addStretch()

        # Right side - Import/Export buttons in vertical layout
        import_export_layout = QtWidgets.QVBoxLayout()
        import_export_layout.setSpacing(5)

        # Export PDF button
        self.btn_export_pdf = QtWidgets.QPushButton("EXPORT PDF")
        self.btn_export_pdf.setFont(font_btn)
        self.btn_export_pdf.setFixedHeight(30)
        self.btn_export_pdf.setStyleSheet(danger_button_style)
        self.btn_export_pdf.clicked.connect(self.export_pdf)

        # Export Excel button
        self.btn_export_excel = QtWidgets.QPushButton("EXPORT EXCEL")
        self.btn_export_excel.setFont(font_btn)
        self.btn_export_excel.setFixedHeight(30)
        self.btn_export_excel.setStyleSheet(success_button_style)
        self.btn_export_excel.clicked.connect(self.export_excel)

        # Import Excel button
        self.btn_import_excel = QtWidgets.QPushButton("IMPORT EXCEL")
        self.btn_import_excel.setFont(font_btn)
        self.btn_import_excel.setFixedHeight(30)
        self.btn_import_excel.setStyleSheet(warning_button_style)
        self.btn_import_excel.clicked.connect(self.import_excel)

        import_export_layout.addWidget(self.btn_export_pdf)
        import_export_layout.addWidget(self.btn_export_excel)
        import_export_layout.addWidget(self.btn_import_excel)

        buttons_main_layout.addLayout(import_export_layout)

        self.scrollLayout.addLayout(buttons_main_layout)

        # --- Export Options Checkbox ---
        export_options_layout = QtWidgets.QHBoxLayout()

        self.include_charts_checkbox = QtWidgets.QCheckBox("Include charts and statistics in Excel export")
        self.include_charts_checkbox.setChecked(True)
        self.include_charts_checkbox.setStyleSheet("color: black; font-weight: bold; font-size: 11px;")
        self.include_charts_checkbox.setToolTip(
            "When checked, Excel exports will include additional sheets with charts data and statistical analysis")

        export_options_layout.addWidget(self.include_charts_checkbox)
        export_options_layout.addStretch()

        self.scrollLayout.addLayout(export_options_layout)

    def create_graphs(self):
        font_label = QtGui.QFont()
        font_label.setPointSize(12)
        font_label.setBold(True)

        # Activity Graph
        self.label_activity_graph = QtWidgets.QLabel("Activity Overview")
        self.label_activity_graph.setFont(font_label)
        self.label_activity_graph.setStyleSheet("color: black;")

        self.chart_view_activity = QChartView()
        self.chart_view_activity.setMinimumHeight(250)
        self.chart_view_activity.setStyleSheet(
            "background-color: white; border-radius: 8px; border: 1px solid #e2e8f0;")

        # Users Graph
        self.label_users_graph = QtWidgets.QLabel("Users Growth")
        self.label_users_graph.setFont(font_label)
        self.label_users_graph.setStyleSheet("color: black;")

        self.chart_view_users = QChartView()
        self.chart_view_users.setMinimumHeight(250)
        self.chart_view_users.setStyleSheet("background-color: white; border-radius: 8px; border: 1px solid #e2e8f0;")

    def update_data_cards(self):
        """Update data cards with real statistics"""
        try:
            db = Database()

            print("🔄 Loading quick stats for Reports Window...")

            # Total Books
            total_books = db.fetch_one("SELECT COUNT(*) as count FROM books")
            total_books_count = total_books['count'] if total_books else 0

            # Active Users
            active_users = db.fetch_one("SELECT COUNT(*) as count FROM users WHERE status = 'Active'")
            active_users_count = active_users['count'] if active_users else 0

            # BORROWED BOOKS (currently active borrows)
            borrowed = db.fetch_one("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'borrow' AND status = 'active'
            """)
            borrowed_count = borrowed['count'] if borrowed else 0

            # RETURNED BOOKS (historical returns)
            returned = db.fetch_one("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'borrow' AND status = 'returned'
            """)
            returned_count = returned['count'] if returned else 0

            # OVERDUE BOOKS - COUNT HISTORICAL OVERDUES (books that were returned late)
            overdue = db.fetch_one("""
                SELECT COUNT(*) as count FROM transactions 
                WHERE transaction_type = 'borrow' 
                AND status = 'returned'
                AND return_date > due_date
            """)
            overdue_count = overdue['count'] if overdue else 0

            print(f"📊 Reports Window Counts:")
            print(f"  - Books: {total_books_count}")
            print(f"  - Active Users: {active_users_count}")
            print(f"  - Borrowed (active): {borrowed_count}")
            print(f"  - Returned: {returned_count}")
            print(f"  - Historical Overdues: {overdue_count}")

            # Update data cards
            self.label_total_books_value.setText(str(total_books_count))
            self.label_borrowed_books_value.setText(str(borrowed_count))
            self.label_overdue_books_value.setText(str(overdue_count))
            self.label_returned_books_value.setText(str(returned_count))

            # Total Transactions
            total_transactions = db.fetch_one("SELECT COUNT(*) as count FROM transactions")
            total_transactions_count = total_transactions['count'] if total_transactions else 0
            self.label_total_transactions_value.setText(str(total_transactions_count))

        except Exception as e:
            print(f"❌ Error updating data cards in Reports Window: {e}")
            # Set default values on error
            self.label_total_books_value.setText("0")
            self.label_borrowed_books_value.setText("0")
            self.label_overdue_books_value.setText("0")
            self.label_returned_books_value.setText("0")
            self.label_total_transactions_value.setText("0")

    def update_graphs(self):
        period = self.comboBox_graph_period.currentText()
        self.create_activity_chart(period)
        self.create_users_chart(period)

    def create_activity_chart(self, period):
        chart = QChart()
        chart.setTitle("Library Activity")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        try:
            db = Database()

            if period == "Daily":
                # Get last 7 days data
                query = """
                    SELECT DATE(created_at) as date,
                           COUNT(CASE WHEN transaction_type = 'borrow' THEN 1 END) as borrows,
                           COUNT(CASE WHEN transaction_type = 'return' THEN 1 END) as returns
                    FROM transactions
                    WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
                    GROUP BY DATE(created_at)
                    ORDER BY date
                """
                data = db.fetch_all(query)
                categories = [str(item['date']) for item in data]

                set_borrowed = QBarSet("Borrowed")
                set_returned = QBarSet("Returned")

                for item in data:
                    set_borrowed.append(item['borrows'])
                    set_returned.append(item['returns'])

            elif period == "Monthly":
                # Get last 6 months data
                query = """
                    SELECT DATE_FORMAT(created_at, '%Y-%m') as month,
                           COUNT(CASE WHEN transaction_type = 'borrow' THEN 1 END) as borrows,
                           COUNT(CASE WHEN transaction_type = 'return' THEN 1 END) as returns
                    FROM transactions
                    WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
                    GROUP BY DATE_FORMAT(created_at, '%Y-%m')
                    ORDER BY month
                """
                data = db.fetch_all(query)
                categories = [str(item['month']) for item in data]

                set_borrowed = QBarSet("Borrowed")
                set_returned = QBarSet("Returned")

                for item in data:
                    set_borrowed.append(item['borrows'])
                    set_returned.append(item['returns'])

            else:  # Yearly
                # Get last 5 years data
                query = """
                    SELECT YEAR(created_at) as year,
                           COUNT(CASE WHEN transaction_type = 'borrow' THEN 1 END) as borrows,
                           COUNT(CASE WHEN transaction_type = 'return' THEN 1 END) as returns
                    FROM transactions
                    GROUP BY YEAR(created_at)
                    ORDER BY year
                    LIMIT 5
                """
                data = db.fetch_all(query)
                categories = [str(item['year']) for item in data]

                set_borrowed = QBarSet("Borrowed")
                set_returned = QBarSet("Returned")

                for item in data:
                    set_borrowed.append(item['borrows'])
                    set_returned.append(item['returns'])

            set_borrowed.setColor(QtGui.QColor("#3B82F6"))
            set_returned.setColor(QtGui.QColor("#10B981"))

            series = QBarSeries()
            series.append(set_borrowed)
            series.append(set_returned)
            chart.addSeries(series)

            # Create axes
            axis_x = QBarCategoryAxis()
            axis_x.append(categories)
            chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
            series.attachAxis(axis_x)

            axis_y = QValueAxis()
            max_value = max([max(set_borrowed.values()), max(set_returned.values())]) if data else 10
            axis_y.setRange(0, max_value + 2)
            chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)
            series.attachAxis(axis_y)

            chart.legend().setVisible(True)
            chart.legend().setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        except Exception as e:
            print(f"Error creating activity chart: {e}")
            chart.setTitle("Library Activity - No Data Available")

        self.chart_view_activity.setChart(chart)

    def create_users_chart(self, period):
        chart = QChart()
        chart.setTitle("Users Growth")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        try:
            db = Database()
            series = QLineSeries()
            series.setName("Total Users")

            if period == "Daily":
                query = """
                    SELECT DATE(created_at) as date, COUNT(*) as cumulative
                    FROM users
                    WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 7 DAY)
                    GROUP BY DATE(created_at)
                    ORDER BY date
                """
            elif period == "Monthly":
                query = """
                    SELECT DATE_FORMAT(created_at, '%Y-%m') as month, COUNT(*) as cumulative
                    FROM users
                    WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
                    GROUP BY DATE_FORMAT(created_at, '%Y-%m')
                    ORDER BY month
                """
            else:  # Yearly
                query = """
                    SELECT YEAR(created_at) as year, COUNT(*) as cumulative
                    FROM users
                    GROUP BY YEAR(created_at)
                    ORDER BY year
                    LIMIT 5
                """

            data = db.fetch_all(query)

            if data:
                for i, item in enumerate(data):
                    if period == "Daily":
                        series.append(i, item['cumulative'])
                    elif period == "Monthly":
                        series.append(i, item['cumulative'])
                    else:
                        series.append(i, item['cumulative'])

                categories = [list(item.values())[0] for item in data]
            else:
                # No data available
                categories = ["No Data"]

            series.setColor(QtGui.QColor("#EC4899"))
            chart.addSeries(series)

            # Create axes
            axis_x = QBarCategoryAxis()
            axis_x.append(categories)
            chart.addAxis(axis_x, QtCore.Qt.AlignmentFlag.AlignBottom)
            series.attachAxis(axis_x)

            axis_y = QValueAxis()
            max_value = max([item['cumulative'] for item in data]) if data else 10
            axis_y.setRange(0, max_value + 2)
            chart.addAxis(axis_y, QtCore.Qt.AlignmentFlag.AlignLeft)
            series.attachAxis(axis_y)

            chart.legend().setVisible(True)
            chart.legend().setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        except Exception as e:
            print(f"Error creating users chart: {e}")
            chart.setTitle("Users Growth - No Data Available")

        self.chart_view_users.setChart(chart)

    def generate_report(self):
        report_type = self.comboBox_report_type.currentText()
        date_from = self.dateEdit_from.date().toString("yyyy-MM-dd")
        date_to = self.dateEdit_to.date().toString("yyyy-MM-dd")

        # Update data cards and graphs
        self.update_data_cards()
        self.update_graphs()

        # Generate different report content based on report type
        if report_type == "Summary Report":
            report_content = self.generate_summary_report(date_from, date_to)
        elif report_type == "Folder Report":
            report_content = self.generate_folder_report(date_from, date_to)
        else:
            report_content = self.generate_generic_report(report_type, date_from, date_to)

        self.textEdit_report.setPlainText(report_content)
        QtWidgets.QMessageBox.information(None, "Report Generated",
                                          f"{report_type} generated for the period {date_from} to {date_to}")

    def generate_summary_report(self, date_from, date_to):
        """Generate summary report with real data"""
        try:
            db = Database()

            # Get statistics
            total_books = db.fetch_one("SELECT COUNT(*) as count FROM books")['count']
            available_books = db.fetch_one("SELECT SUM(available) as total FROM books")['total'] or 0
            total_users = db.fetch_one("SELECT COUNT(*) as count FROM users WHERE status = 'Active'")['count']

            # Get transactions in date range
            transactions_query = """
                SELECT COUNT(*) as count, transaction_type 
                FROM transactions 
                WHERE DATE(created_at) BETWEEN %s AND %s 
                GROUP BY transaction_type
            """
            transactions = db.fetch_all(transactions_query, (date_from, date_to))

            borrow_count = 0
            return_count = 0
            for trans in transactions:
                if trans['transaction_type'] == 'borrow':
                    borrow_count = trans['count']
                elif trans['transaction_type'] == 'return':
                    return_count = trans['count']

            # Get popular books
            popular_books_query = """
                SELECT book_title, COUNT(*) as borrow_count
                FROM transactions 
                WHERE transaction_type = 'borrow' 
                AND DATE(created_at) BETWEEN %s AND %s
                GROUP BY book_title 
                ORDER BY borrow_count DESC 
                LIMIT 5
            """
            popular_books = db.fetch_all(popular_books_query, (date_from, date_to))

            popular_books_text = ""
            for i, book in enumerate(popular_books, 1):
                popular_books_text += f"{i}. {book['book_title']} ({book['borrow_count']} borrows)\n"

            if not popular_books_text:
                popular_books_text = "No borrowing data available\n"

            return f"""
LIBRARY MANAGEMENT SYSTEM - SUMMARY REPORT
Date Range: {date_from} to {date_to}
Generated on: {QtCore.QDate.currentDate().toString("yyyy-MM-dd")}

===== QUICK STATISTICS =====

Total Books: {total_books}
Available Books: {available_books}
Currently Borrowed: {borrow_count - return_count}
Active Users: {total_users}

===== ACTIVITY SUMMARY =====

Books Borrowed: {borrow_count}
Books Returned: {return_count}
Total Transactions: {borrow_count + return_count}

===== POPULAR BOOKS =====

{popular_books_text}
===== SYSTEM OVERVIEW =====

The library management system is operating normally.
All modules are functional and connected to the database.

--- END OF SUMMARY REPORT ---
"""

        except Exception as e:
            return f"Error generating report: {str(e)}"

    def generate_folder_report(self, date_from, date_to):
        return f"""
        FOLDER REPORT
        Date Range: {date_from} to {date_to}
        Generated on: {QtCore.QDate.currentDate().toString("yyyy-MM-dd")}

        ===== FOLDER STRUCTURE OVERVIEW =====

        MAIN FOLDERS:
        - Books Database
        - User Records  
        - Transaction History
        - System Logs
        - Reports Archive

        ===== SYSTEM INFORMATION =====

        Database: library_db
        Tables: books, users, transactions
        Total Records: {self.label_total_books_value.text()} books, {self.label_total_transactions_value.text()} transactions
        System Status: Operational

        --- END OF FOLDER REPORT ---
        """

    def generate_generic_report(self, report_type, date_from, date_to):
        return f"""
        REPORT: {report_type}
        DATE RANGE: {date_from} to {date_to}
        GENERATED ON: {QtCore.QDate.currentDate().toString("yyyy-MM-dd")}

        This is a sample {report_type.lower()}. 

        Current system statistics:
        - Total Books: {self.label_total_books_value.text()}
        - Borrowed Books: {self.label_borrowed_books_value.text()}
        - Overdue Books: {self.label_overdue_books_value.text()}
        - Returned Books: {self.label_returned_books_value.text()}
        - Total Transactions: {self.label_total_transactions_value.text()}

        The system is connected to the database and showing real-time statistics.

        --- END OF REPORT ---
        """

    def export_pdf(self):
        QtWidgets.QMessageBox.information(None, "Export PDF",
                                          "PDF export functionality will be implemented when system is complete")

    def export_excel(self):
        """Enhanced Excel export with chart options"""
        try:
            # Get export options from user
            dialog = ExportOptionsDialog()
            result = dialog.exec()

            if result != QtWidgets.QDialog.DialogCode.Accepted:
                return  # User cancelled

            export_type = dialog.get_export_type()
            include_charts = dialog.get_include_charts()

            # Generate filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            default_filename = f"library_export_{export_type}_{timestamp}.xlsx"

            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
                None,
                "Export to Excel",
                default_filename,
                "Excel Files (*.xlsx);;All Files (*)"
            )

            if not file_path:
                return  # User cancelled

            db = Database()

            with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
                # Export main data based on type
                if export_type == "books":
                    data = db.fetch_all("SELECT * FROM books")
                    df = pd.DataFrame(data)
                    df.to_excel(writer, sheet_name='Books', index=False)

                elif export_type == "users":
                    data = db.fetch_all("SELECT * FROM users")
                    df = pd.DataFrame(data)
                    df.to_excel(writer, sheet_name='Users', index=False)

                elif export_type == "transactions":
                    data = db.fetch_all("""
                        SELECT t.*, b.title as book_title, u.name as user_name 
                        FROM transactions t
                        LEFT JOIN books b ON t.book_id = b.id
                        LEFT JOIN users u ON t.user_id = u.id
                    """)
                    df = pd.DataFrame(data)
                    df.to_excel(writer, sheet_name='Transactions', index=False)

                elif export_type == "summary":
                    # Export multiple sheets for summary
                    self.export_summary_report(writer, db)

                # Add charts if requested
                if include_charts:
                    self.export_charts_to_excel(writer, db)

            # Show export summary
            chart_status = "with charts and statistics" if include_charts else "without charts"
            QtWidgets.QMessageBox.information(
                None,
                "Export Successful",
                f"✅ {export_type.title()} data exported successfully!\n\n"
                f"📊 Export type: {chart_status}\n"
                f"📁 File: {os.path.basename(file_path)}\n"
                f"📅 Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            )

        except ImportError:
            QtWidgets.QMessageBox.critical(
                None,
                "Missing Dependency",
                "❌ Excel export requires pandas library.\n\n"
                "Please install it using:\n"
                "pip install pandas openpyxl"
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                None,
                "Export Error",
                f"❌ Failed to export Excel file: {str(e)}"
            )

    def export_summary_report(self, writer, db):
        """Export summary report with multiple sheets"""
        try:
            # Sheet 1: Library Statistics
            stats_data = {
                'Metric': ['Total Books', 'Total Users', 'Active Borrows', 'Overdue Books', 'Total Transactions'],
                'Value': [
                    self.label_total_books_value.text(),
                    self.label_borrowed_books_value.text(),
                    self.label_overdue_books_value.text(),
                    self.label_returned_books_value.text(),
                    self.label_total_transactions_value.text()
                ]
            }
            stats_df = pd.DataFrame(stats_data)
            stats_df.to_excel(writer, sheet_name='Library Statistics', index=False)

            # Sheet 2: Recent Transactions
            recent_transactions = db.fetch_all("""
                SELECT t.transaction_type, t.borrow_date, t.due_date, t.return_date, t.status,
                       b.title as book_title, u.name as user_name
                FROM transactions t
                LEFT JOIN books b ON t.book_id = b.id
                LEFT JOIN users u ON t.user_id = u.id
                ORDER BY t.created_at DESC
                LIMIT 100
            """)
            if recent_transactions:
                trans_df = pd.DataFrame(recent_transactions)
                trans_df.to_excel(writer, sheet_name='Recent Transactions', index=False)

            # Sheet 3: Popular Books
            popular_books = db.fetch_all("""
                SELECT b.title, b.author, b.genre, 
                       COUNT(t.id) as borrow_count,
                       b.available as available_copies
                FROM books b
                LEFT JOIN transactions t ON b.id = t.book_id AND t.transaction_type = 'borrow'
                GROUP BY b.id, b.title, b.author, b.genre, b.available
                ORDER BY borrow_count DESC
                LIMIT 20
            """)
            if popular_books:
                popular_df = pd.DataFrame(popular_books)
                popular_df.to_excel(writer, sheet_name='Popular Books', index=False)

        except Exception as e:
            print(f"Error exporting summary report: {e}")

    def export_charts_to_excel(self, writer, db):
        """Export chart data to Excel"""
        try:
            # Monthly activity data
            monthly_activity = db.fetch_all("""
                SELECT DATE_FORMAT(created_at, '%Y-%m') as month,
                       COUNT(CASE WHEN transaction_type = 'borrow' THEN 1 END) as borrows,
                       COUNT(CASE WHEN transaction_type = 'return' THEN 1 END) as returns
                FROM transactions
                WHERE created_at >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)
                GROUP BY DATE_FORMAT(created_at, '%Y-%m')
                ORDER BY month
            """)

            if monthly_activity:
                activity_df = pd.DataFrame(monthly_activity)
                activity_df.to_excel(writer, sheet_name='Monthly Activity', index=False)

        except Exception as e:
            print(f"Error exporting charts: {e}")

    def import_excel(self):
        """Import data from Excel file"""
        try:
            # Open file dialog to select Excel file
            file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
                None,
                "Select Excel File to Import",
                "",
                "Excel Files (*.xlsx *.xls);;All Files (*)"
            )

            if not file_path:
                return  # User cancelled

            # Read the Excel file
            df = pd.read_excel(file_path)

            # Show import options dialog
            dialog = ImportOptionsDialog(df.columns.tolist())
            result = dialog.exec()

            if result == QtWidgets.QDialog.DialogCode.Accepted:
                import_type = dialog.get_import_type()
                column_mapping = dialog.get_column_mapping()

                # Process the import based on type
                if import_type == "books":
                    self.import_books_data(df, column_mapping)
                elif import_type == "users":
                    self.import_users_data(df, column_mapping)
                elif import_type == "transactions":
                    self.import_transactions_data(df, column_mapping)
                else:
                    QtWidgets.QMessageBox.warning(None, "Import Error", "Invalid import type selected")

        except ImportError:
            QtWidgets.QMessageBox.critical(
                None,
                "Missing Dependency",
                "❌ Excel import requires pandas library.\n\n"
                "Please install it using:\n"
                "pip install pandas openpyxl"
            )
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Import Error", f"❌ Failed to import Excel file: {str(e)}")

    def import_books_data(self, df, column_mapping):
        """Import books data from Excel"""
        try:
            db = Database()
            imported_count = 0
            skipped_count = 0

            for _, row in df.iterrows():
                try:
                    # Map columns based on user selection
                    title = row[column_mapping['title']] if 'title' in column_mapping else None
                    author = row[column_mapping['author']] if 'author' in column_mapping else "Unknown"
                    isbn = row[column_mapping['isbn']] if 'isbn' in column_mapping else ""
                    genre = row[column_mapping['genre']] if 'genre' in column_mapping else "General"
                    year = row[column_mapping['year']] if 'year' in column_mapping else 2024
                    total_copies = row[column_mapping['total_copies']] if 'total_copies' in column_mapping else 1
                    available_copies = row[
                        column_mapping['available_copies']] if 'available_copies' in column_mapping else total_copies

                    if not title:
                        skipped_count += 1
                        continue

                    # Check if book already exists (by title or ISBN)
                    existing_book = db.fetch_one(
                        "SELECT id FROM books WHERE title = %s OR isbn = %s",
                        (title, isbn)
                    )

                    if existing_book:
                        skipped_count += 1
                        continue

                    # Insert new book
                    query = """
                        INSERT INTO books (title, author, isbn, genre, publication_year, total_copies, available)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    db.execute_query(query, (title, author, isbn, genre, year, total_copies, available_copies))
                    imported_count += 1

                except Exception as e:
                    print(f"Error importing book row: {e}")
                    skipped_count += 1

            # Update data cards and show success message
            self.update_data_cards()
            QtWidgets.QMessageBox.information(
                None,
                "Import Successful",
                f"✅ Successfully imported {imported_count} books.\n"
                f"⏭️ Skipped {skipped_count} duplicate/invalid books."
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Import Error", f"❌ Failed to import books: {str(e)}")

    def import_users_data(self, df, column_mapping):
        """Import users data from Excel"""
        try:
            db = Database()
            imported_count = 0
            skipped_count = 0

            for _, row in df.iterrows():
                try:
                    # Map columns based on user selection
                    user_id = row[column_mapping['user_id']] if 'user_id' in column_mapping else None
                    name = row[column_mapping['name']] if 'name' in column_mapping else "Unknown"
                    email = row[column_mapping['email']] if 'email' in column_mapping else ""
                    phone = row[column_mapping['phone']] if 'phone' in column_mapping else ""
                    department = row[column_mapping['department']] if 'department' in column_mapping else "General"

                    if not user_id or not name:
                        skipped_count += 1
                        continue

                    # Check if user already exists
                    existing_user = db.fetch_one(
                        "SELECT id FROM users WHERE user_id = %s OR email = %s",
                        (user_id, email)
                    )

                    if existing_user:
                        skipped_count += 1
                        continue

                    # Insert new user
                    query = """
                        INSERT INTO users (user_id, name, email, phone, department, status)
                        VALUES (%s, %s, %s, %s, %s, 'Active')
                    """
                    db.execute_query(query, (user_id, name, email, phone, department))
                    imported_count += 1

                except Exception as e:
                    print(f"Error importing user row: {e}")
                    skipped_count += 1

            # Update data cards and show success message
            self.update_data_cards()
            QtWidgets.QMessageBox.information(
                None,
                "Import Successful",
                f"✅ Successfully imported {imported_count} users.\n"
                f"⏭️ Skipped {skipped_count} duplicate/invalid users."
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Import Error", f"❌ Failed to import users: {str(e)}")

    def import_transactions_data(self, df, column_mapping):
        """Import transactions data from Excel"""
        try:
            db = Database()
            imported_count = 0
            skipped_count = 0

            for _, row in df.iterrows():
                try:
                    # Map columns based on user selection
                    book_title = row[column_mapping['book_title']] if 'book_title' in column_mapping else None
                    user_name = row[column_mapping['user_name']] if 'user_name' in column_mapping else None
                    transaction_type = row[
                        column_mapping['transaction_type']] if 'transaction_type' in column_mapping else "borrow"
                    borrow_date = row[
                        column_mapping['borrow_date']] if 'borrow_date' in column_mapping else datetime.now().date()
                    due_date = row[column_mapping['due_date']] if 'due_date' in column_mapping else None
                    return_date = row[column_mapping['return_date']] if 'return_date' in column_mapping else None
                    status = row[column_mapping['status']] if 'status' in column_mapping else "active"

                    if not book_title or not user_name:
                        skipped_count += 1
                        continue

                    # Get book ID
                    book = db.fetch_one("SELECT id FROM books WHERE title = %s", (book_title,))
                    if not book:
                        skipped_count += 1
                        continue

                    # Get user ID
                    user = db.fetch_one("SELECT id FROM users WHERE name = %s", (user_name,))
                    if not user:
                        skipped_count += 1
                        continue

                    # Insert transaction
                    query = """
                        INSERT INTO transactions (book_id, user_id, transaction_type, borrow_date, due_date, return_date, status, book_title, user_name)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    db.execute_query(query, (
                        book['id'], user['id'], transaction_type, borrow_date,
                        due_date, return_date, status, book_title, user_name
                    ))
                    imported_count += 1

                except Exception as e:
                    print(f"Error importing transaction row: {e}")
                    skipped_count += 1

            # Update data cards and show success message
            self.update_data_cards()
            QtWidgets.QMessageBox.information(
                None,
                "Import Successful",
                f"✅ Successfully imported {imported_count} transactions.\n"
                f"⏭️ Skipped {skipped_count} invalid transactions."
            )

        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Import Error", f"❌ Failed to import transactions: {str(e)}")

    def create_test_data_if_empty(self):
        """Create test data if database is empty - for debugging"""
        try:
            db = Database()

            # Check if we have any transactions
            transaction_count = db.fetch_one("SELECT COUNT(*) as count FROM transactions")['count']

            if transaction_count == 0:
                print("No transactions found. Creating test data...")

                # Get a book and user to use for test data
                books = db.fetch_all("SELECT id, title FROM books LIMIT 1")
                users = db.fetch_all("SELECT id, user_id FROM users LIMIT 1")

                if books and users:
                    book_id = books[0]['id']
                    user_id = users[0]['id']
                    book_title = books[0]['title']
                    user_name = "Test User"

                    # Create test borrow transaction (overdue)
                    borrow_query = """
                        INSERT INTO transactions (book_id, user_id, transaction_type, borrow_date, due_date, status, book_title, user_name)
                        VALUES (%s, %s, 'borrow', DATE_SUB(CURDATE(), INTERVAL 20 DAY), DATE_SUB(CURDATE(), INTERVAL 5 DAY), 'active', %s, %s)
                    """
                    db.execute_query(borrow_query, (book_id, user_id, book_title, user_name))

                    # Create test borrow transaction (not overdue)
                    borrow_query2 = """
                        INSERT INTO transactions (book_id, user_id, transaction_type, borrow_date, due_date, status, book_title, user_name)
                        VALUES (%s, %s, 'borrow', CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY), 'active', %s, %s)
                    """
                    db.execute_query(borrow_query2, (book_id, user_id, book_title, user_name))

                    # Create test return transaction
                    return_query = """
                        INSERT INTO transactions (book_id, user_id, transaction_type, return_date, status, book_title, user_name)
                        VALUES (%s, %s, 'return', CURDATE(), 'returned', %s, %s)
                    """
                    db.execute_query(return_query, (book_id, user_id, book_title, user_name))

                    print("Test data created successfully!")
                else:
                    print("Cannot create test data - no books or users found in database")
            else:
                print(f"Database already has {transaction_count} transactions")

        except Exception as e:
            print(f"Error creating test data: {e}")


class ImportOptionsDialog(QtWidgets.QDialog):
    def __init__(self, columns, parent=None):
        super().__init__(parent)
        self.columns = columns
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Import Options")
        self.setFixedSize(400, 500)
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QLabel {
                color: #333;
                font-weight: bold;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }
        """)

        layout = QtWidgets.QVBoxLayout()

        # Import type selection
        type_layout = QtWidgets.QHBoxLayout()
        type_layout.addWidget(QtWidgets.QLabel("Import Type:"))
        self.import_type = QtWidgets.QComboBox()
        self.import_type.addItems(["books", "users", "transactions"])
        type_layout.addWidget(self.import_type)
        type_layout.addStretch()
        layout.addLayout(type_layout)

        # Column mapping section
        layout.addWidget(QtWidgets.QLabel("Map Excel Columns to Database Fields:"))

        # Create scroll area for column mapping
        scroll_area = QtWidgets.QScrollArea()
        scroll_widget = QtWidgets.QWidget()
        self.mapping_layout = QtWidgets.QVBoxLayout(scroll_widget)

        self.column_mappings = {}

        # Add mapping fields based on import type
        self.add_mapping_fields()

        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(300)
        layout.addWidget(scroll_area)

        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.ok_btn = QtWidgets.QPushButton("Import")
        self.ok_btn.setStyleSheet(success_button_style)
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.cancel_btn.setStyleSheet(danger_button_style)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(self.ok_btn)
        button_layout.addWidget(self.cancel_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Connect import type change
        self.import_type.currentTextChanged.connect(self.add_mapping_fields)

    def add_mapping_fields(self):
        # Clear existing mapping fields
        for i in reversed(range(self.mapping_layout.count())):
            self.mapping_layout.itemAt(i).widget().setParent(None)

        import_type = self.import_type.currentText()
        self.column_mappings = {}

        if import_type == "books":
            fields = ["title", "author", "isbn", "genre", "year", "total_copies", "available_copies"]
        elif import_type == "users":
            fields = ["user_id", "name", "email", "phone", "department"]
        else:  # transactions
            fields = ["book_title", "user_name", "transaction_type", "borrow_date", "due_date", "return_date", "status"]

        for field in fields:
            row_layout = QtWidgets.QHBoxLayout()
            row_layout.addWidget(QtWidgets.QLabel(f"{field.replace('_', ' ').title()}:"))

            combo = QtWidgets.QComboBox()
            combo.addItem("-- Not Mapped --")
            combo.addItems(self.columns)
            row_layout.addWidget(combo)

            self.mapping_layout.addLayout(row_layout)
            self.column_mappings[field] = combo

    def get_import_type(self):
        return self.import_type.currentText()

    def get_column_mapping(self):
        mapping = {}
        for field, combo in self.column_mappings.items():
            if combo.currentText() != "-- Not Mapped --":
                mapping[field] = combo.currentText()
        return mapping


class ExportOptionsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Export Options")
        self.setFixedSize(300, 200)
        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QLabel {
                color: #333;
                font-weight: bold;
            }
        """)

        layout = QtWidgets.QVBoxLayout()

        # Export type
        layout.addWidget(QtWidgets.QLabel("Export Type:"))
        self.export_type = QtWidgets.QComboBox()
        self.export_type.addItems(["books", "users", "transactions", "summary"])
        layout.addWidget(self.export_type)

        # Include charts checkbox - THIS IS THE CHECKBOX
        self.include_charts = QtWidgets.QCheckBox("Include charts and statistics")
        self.include_charts.setChecked(True)
        self.include_charts.setToolTip("Adds additional sheets with charts data and analysis")
        layout.addWidget(self.include_charts)

        layout.addStretch()

        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        self.ok_btn = QtWidgets.QPushButton("Export")
        self.ok_btn.setStyleSheet(success_button_style)
        self.cancel_btn = QtWidgets.QPushButton("Cancel")
        self.cancel_btn.setStyleSheet(danger_button_style)

        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(self.ok_btn)
        button_layout.addWidget(self.cancel_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def get_export_type(self):
        return self.export_type.currentText()

    def get_include_charts(self):
        return self.include_charts.isChecked()