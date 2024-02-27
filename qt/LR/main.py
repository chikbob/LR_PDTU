# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFrame, QFormLayout, QSpinBox, QLabel, QSlider, \
    QBoxLayout, QVBoxLayout, QHBoxLayout, QPushButton, QDial


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LR2')
        self.setMinimumWidth(300)

        layout = QHBoxLayout()
        self.setLayout(layout)

        spinBox = QSpinBox(minimum=3, maximum=111, value=19)
        slider = QSlider(Qt.Orientation.Horizontal, self)
        label = QLabel('Введіть ваш вік')
        btn = QPushButton("Завершення")
        qDial = QDial()

        slider.setRange(3, 111)
        slider.setValue(19)

        qDial.setRange(3, 111)
        qDial.setValue(19)

        spinBox.valueChanged.connect(slider.setValue)
        slider.valueChanged.connect(spinBox.setValue)
        qDial.valueChanged.connect(spinBox.setValue)
        btn.clicked.connect(self.close)

        layout.addWidget(spinBox)
        layout.addWidget(slider)
        layout.addWidget(label)
        layout.addWidget(qDial)
        layout.addWidget(btn)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
