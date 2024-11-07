"""
Description: A To-Do List application that allows users to add tasks, modify their status, and save the tasks to a CSV file.

Author: Noah Manaigre
"""

from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QMessageBox, QVBoxLayout, QWidget, QTableWidgetItem, QComboBox

from PySide6.QtCore import Slot

from to_do_list.task_editor import TaskEditor

import csv

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initialize_widgets()

        self.add_button.clicked.connect(self.on_add_task)

        self.task_table.cellClicked.connect(self.on_edit_task)

        self.save_button.clicked.connect(self.__save_to_csv)

    def __initialize_widgets(self):
        """
        Given:  Code to create and initialize the QWindow
        and all of the widgets on the window.
        DO NOT EDIT.
        """
        self.setWindowTitle("To-Do List")

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("New Task")

        self.status_combo = QComboBox(self)
        self.status_combo.addItems(["Backlog", "In Progress", "Done"])

        self.add_button = QPushButton("Add Task", self)

        self.save_button = QPushButton("Save to CSV", self)
        
        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Task", "Status"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.task_input)
        layout.addWidget(self.status_combo)
        layout.addWidget(self.add_button)
        layout.addWidget(self.task_table)
        layout.addWidget(self.save_button)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def on_add_task(self):
        task_name = self.task_input.text()
        task_status = self.status_combo.currentText()

        if task_name:
            row_count = self.task_table.rowCount()
            self.task_table.insertRow(row_count)

            task_item = QTableWidgetItem(task_name)
            status_item = QTableWidgetItem(task_status)

            self.task_table.setItem(row_count, 0, task_item)
            self.task_table.setItem(row_count, 1, status_item)

            self.status_label.setText(f"Added task: {task_name}")
            self.task_input.clear()
        else:
            self.status_label.setText("Please enter a task and select its status.")

    def __on_remove_task(self):
        pass

    @Slot(int, int)
    def on_edit_task(self, row, column):
        current_status = self.task_table.item(row, 1).text()

        task_editor = TaskEditor(row, current_status)

        task_editor.exec()

    def update_task_status(self, row: int, new_status: str):
        
        self.task_table.item(row, 1).setText(new_status)

        self.status_label.setText(f"Updated task status to: {new_status}")

    # Part 3
    def __load_data(self, file_path: str):
        """
        Reads data from the .csv file provided.
        Calls the __add_table_row method (to be implemented) 
        for each row of data.
        Args:
            file_path (str): The name of the file (including relative path).
        """
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            
            header = next(reader)  
            for row in reader:
                self.__add_table_row(row)
    
    def __add_table_row(self, row_data):
        """
        Adds a new row to the task_table based on the data passed.
        """
        task_name, task_status = row_data
        row_count = self.task_table.rowCount()
        self.task_table.insertRow(row_count)

        task_item = QTableWidgetItem(task_name)
        status_item = QTableWidgetItem(task_status)

        self.task_table.setItem(row_count, 0, task_item)
        self.task_table.setItem(row_count, 1, status_item)

    def __save_to_csv(self):
        """
        Saves the QTable data to a file.
        """
        file_path = 'output/todos.csv'
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            writer.writerow(["Task", "Status"])

            for row in range(self.task_table.rowCount()):
                task_item = self.task_table.item(row, 0).text()
                status_item = self.task_table.item(row, 1).text()
                writer.writerow([task_item, status_item])

        self.status_label.setText("Tasks saved to todo.csv")
