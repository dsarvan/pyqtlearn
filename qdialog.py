#!/usr/bin/env python
# File: qdialog.py
# Name: D.Saravanan
# Date: 25/07/2024

""" Script to develop dialog-style application using QDialog """


import sys
from PyQt6 import QtWidgets


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QDialog")

        dialogLayout = QtWidgets.QVBoxLayout()

        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Name:", QtWidgets.QLineEdit())
        formLayout.addRow("Age:", QtWidgets.QLineEdit())
        formLayout.addRow("Job:", QtWidgets.QLineEdit())
        formLayout.addRow("Hobbies:", QtWidgets.QLineEdit())

        dialogLayout.addLayout(formLayout)

        buttons = QtWidgets.QDialogButtonBox()
        buttons.setStandardButtons(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel
            | QtWidgets.QDialogButtonBox.StandardButton.Ok
        )

        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
