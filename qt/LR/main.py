# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
# from ui_main import UI_MainWindow

Form, Window = uic.loadUiType("ui_main.ui")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    sys.exit(app.exec())
