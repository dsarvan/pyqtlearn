#!/usr/bin/env python
# File: signalslot.py
# Name: D.Saravanan
# Date: 25/07/2024

""" Script to use the signals and slots mechanism in PyQt6 application """


import sys
from functools import partial

from PyQt6 import QtWidgets


def greet(mlabel, name):
    mlabel.setText("") if mlabel.text() else mlabel.setText(f"Hello, {name}!")


def qvboxlayout():
    """creates a QVBoxLayout object"""
    layout = QtWidgets.QVBoxLayout()
    mlabel = QtWidgets.QLabel("")
    button = QtWidgets.QPushButton("Greet")
    button.clicked.connect(partial(greet, mlabel, "Saravanan"))
    layout.addWidget(button)
    layout.addWidget(mlabel)
    return layout


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("Signals and Slots")
    window.setLayout(qvboxlayout())
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
