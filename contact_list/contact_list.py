
"""
Description: Responsible for contact list functions such as adding contacts and removing contacts.

Author: Noah Manaigre
"""

from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox

from PySide6 import QtCore

class ContactList(QMainWindow):
    """
    Contact List Class (QMainWindow). Provides users a 
    way to manage their contacts.
    """
    def __init__(self):
        """
        Initializes a Contact List window in which 
        users can add and remove contact data.
        """
        super().__init__()
        self.__initialize_widgets()
        self.__connect_signals()

    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def __connect_signals(self):
        """
        Connects button clicks to their respective slot functions.
        """
        self.add_button.clicked.connect(self.__on_add_contact)
        self.remove_button.clicked.connect(self.__on_remove_contact)

    @QtCore.Slot()
    def __on_add_contact(self):
        """
        Adds a new contact to the table. Checks that both name 
        and phone fields are filled out first. Clears the fields after.
        """
        name = self.contact_name_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and phone:
            row_position = self.contact_table.rowCount()
            self.contact_table.insertRow(row_position)
            self.contact_table.setItem(row_position, 0, QTableWidgetItem(name))
            self.contact_table.setItem(row_position, 1, QTableWidgetItem(phone))

            self.contact_name_input.clear()
            self.phone_input.clear()
            self.status_label.setText(f"Contact added: {name}")
        else:
            self.status_label.setText("Please enter both name and phone number.")

    @QtCore.Slot()
    def __on_remove_contact(self):
        """
        Slot that is triggered when the Remove Contact button is clicked.
        Confirms removal of the selected contact and removes it from the table.
        """
        selected_row = self.contact_table.currentRow()

        if selected_row >= 0:
            reply = QMessageBox.question(self, "Remove Contact", 
                "Are you sure you want to remove the selected contact?", 
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.contact_table.removeRow(selected_row)
                self.status_label.setText("Contact removed.")
        else:
            self.status_label.setText("Please select a row to be removed.")