# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('LR3')
        self.setMinimumWidth(300)

        layout = QHBoxLayout()
        self.setLayout(layout)

        label = QLabel("<h3>Каталог бібліотеки<h3>"
                       "<table border=\"1\" width=\"500\" style=\"border-color: black\" >"
                       "<tr>"
                       "<td>Автор</td>"
                       "<td>Назва книги</td>"
                       "<td>Рік випуску</td>"
                       "<td>Група</td>"
                       "</tr>"
                       "<tr>"
                       "<td>Сенкевич</td>"
                       "<td>Потоп</td>"
                       "<td>1978</td>"
                       "<td>Х</td>"
                       "</tr>"
                       "<tr>"
                       "<td>Ландау</td>"
                       "<td>Теорія поля</td>"
                       "<td>1989</td>"
                       "<td>У</td>"
                       "</tr>"
                       "<tr>"
                       "<td>Дойль</td>"
                       "<td>Сумчасті</td>"
                       "<td>1990</td>"
                       "<td>C</td>"
                       "</tr>"
                       "</table>"
                       "<div>Примітка:</div>"
                       "<ul>"
                       "<li>Х – художня література;</li>"
                       "<li>У – навчальна література</li>"
                       "<li>З – довідкова література</li>"
                       "</ul>"
                       "<center><img border = \"0\" src = \"icons/mouse.png\"></center>"
                       )

        layout.addWidget(label)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
