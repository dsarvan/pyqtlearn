#!/usr/bin/env python
# File: qgridlayout.py
# Name: D.Saravanan
# Date: 24/07/2024

""" Script to arrange widgets in grid layout using QGridLayout """

import sys
from PyQt6 import QtWidgets


def qgridlayout():
    """creates a QGridLayout object"""
    layout = QtWidgets.QGridLayout()
    layout.addWidget(QtWidgets.QPushButton("Button (0, 0)"), 0, 0)
    layout.addWidget(QtWidgets.QPushButton("Button (0, 1)"), 0, 1)
    layout.addWidget(QtWidgets.QPushButton("Button (0, 2)"), 0, 2)
    layout.addWidget(QtWidgets.QPushButton("Button (1, 0)"), 1, 0)
    layout.addWidget(QtWidgets.QPushButton("Button (1, 1)"), 1, 1)
    layout.addWidget(QtWidgets.QPushButton("Button (1, 2)"), 1, 2)
    layout.addWidget(QtWidgets.QPushButton("Button (2, 0)"), 2, 0)
    layout.addWidget(
        QtWidgets.QPushButton("Button (2, 1) + 2 Columns Span"), 2, 1, 1, 2
    )
    return layout


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("QGridLayout")
    window.setLayout(qgridlayout())
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
