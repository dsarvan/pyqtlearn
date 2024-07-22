#!/usr/bin/env python
# File: qmainwindow.py
# Name: D.Saravanan
# Date: 25/07/2024

""" Script to create main window-style application using QMainWindow """

import sys
from PyQt6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.setCentralWidget(QtWidgets.QLabel("Placeholder Central Widget"))
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tool = QtWidgets.QToolBar()
        tool.addAction("Exit", self.close)
        self.addToolBar(tool)

    def _createStatusBar(self):
        status = QtWidgets.QStatusBar()
        status.showMessage("Placeholder Status Bar")
        self.setStatusBar(status)


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())
