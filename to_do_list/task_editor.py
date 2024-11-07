"""
Description: This class is for the task status

Author: Noah Manaigre
"""

from PySide6.QtWidgets import  QPushButton,  QVBoxLayout,  QComboBox, QDialog

from PySide6.QtCore import Slot

class TaskEditor(QDialog):

    def __init__(self, row: int, status: str):
        super().__init__()
        self.initialize_widgets(row, status)

    def initialize_widgets(self, row: int, status: str):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("Edit Task Status")

        self.row = row

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])
        
        self.save_button = QPushButton("Save", self)

        layout = QVBoxLayout()
        layout.addWidget(self.status_combo)
        layout.addWidget(self.save_button)
        self.setLayout(layout)
        self.setFixedWidth(150)

    @Slot()
    def on_save_status(self):
        """
        Slot to handle the 'Save' button click event.
        Extracts the current text from the status_combo widget and closes the dialog.
        """
        new_status = self.status_combo.currentText()

        self.task_updated.emit(self.row, new_status)

        self.accept()