#!/usr/bin/env python
# File: qformlayout.py
# Name: D.Saravanan
# Date: 24/07/2024

""" Script to arrange widgets in form layout using QFormLayout """

import sys
from PyQt6 import QtWidgets


def qformlayout():
    """create a QFormLayout object"""
    layout = QtWidgets.QFormLayout()
    layout.addRow("Name:", QtWidgets.QLineEdit())
    layout.addRow("Age:", QtWidgets.QLineEdit())
    layout.addRow("Job:", QtWidgets.QLineEdit())
    layout.addRow("Hobbies:", QtWidgets.QLineEdit())
    return layout


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("QFormLayout")
    window.setLayout(qformlayout())
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
