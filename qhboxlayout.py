#!/usr/bin/env python
# File: qhboxlayout.py
# Name: D.Saravanan
# Date: 24/07/2024

""" Script to arrange widgets horizontally using QHBoxLayout """

import sys
from PyQt6 import QtWidgets


def qhboxlayout():
    """creates a QHBoxLayout object"""
    layout = QtWidgets.QHBoxLayout()
    layout.addWidget(QtWidgets.QPushButton("Left"))
    layout.addWidget(QtWidgets.QPushButton("Center"))
    layout.addWidget(QtWidgets.QPushButton("Right"))
    return layout


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()
    window.setWindowTitle("QHBoxLayout")
    window.setLayout(qhboxlayout())
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
