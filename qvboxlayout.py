#!/usr/bin/env python
# File: qvboxlayout.py
# Name: D.Saravanan
# Date: 24/07/2024

""" Script to arrange widgets vertically using QVBoxLayout """


import sys
from PyQt6 import QtWidgets


def qvboxlayout():
    """creates a QVBoxLayout object"""
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(QtWidgets.QPushButton("Top"))
    layout.addWidget(QtWidgets.QPushButton("Center"))
    layout.addWidget(QtWidgets.QPushButton("Bottom"))
    return layout


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("QVBoxLayout")
    window.setLayout(qvboxlayout())
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
