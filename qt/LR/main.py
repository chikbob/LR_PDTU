# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFrame


# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QFrame

# from ui_main import UI_MainWindow

# Form, Window = uic.loadUiType("ui_main.ui")

def createFrame():
    f = QFrame(root)
    f.move(15, 10)
    f.resize(150, 100)
    f.setStyleSheet("background-color: rgb(170,10,10)")
    f.setFrameStyle((QFrame.Panel | QFrame.Shadow.Sunken))
    f.setLineWidth(3)
    f.setMidLineWidth(3)
    f.setCursor(Qt.ForbiddenCursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = QMainWindow()
    root.resize(300, 300)
    root.setWindowTitle("LR1")
    root.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
    root.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
    createFrame()
    root.show()
    sys.exit(app.exec())
