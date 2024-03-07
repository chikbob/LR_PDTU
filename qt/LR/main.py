import sys

from PySide6.QtWidgets import QWidget, QLCDNumber, QGridLayout, QPushButton, QApplication


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.m_strDisplay = ""
        self.m_stk = []
        self.m_plcd = QLCDNumber(12)
        self.m_plcd.setSegmentStyle(QLCDNumber.Flat)
        self.m_plcd.setMinimumSize(150, 50)

        aButtons = [['7', '8', '9', '/'],
                    ['4', '5', '6', '*'],
                    ['1', '2', '3', '-'],
                    ['0', '.', '=', '+']]

        ptopLayout = QGridLayout()
        ptopLayout.addWidget(self.m_plcd, 0, 0, 1, 4)
        ptopLayout.addWidget(self.createButton("CE"), 1, 3)

        for i in range(4):
            for j in range(4):
                ptopLayout.addWidget(self.createButton(aButtons[i][j]), i + 2, j)

        self.setLayout(ptopLayout)

        self.show()

    def createButton(self, text):
        pcmd = QPushButton(text)
        pcmd.setMinimumSize(40, 40)
        pcmd.clicked.connect(self.slotButtonClicked)
        return pcmd

    def calculate(self):
        dOperand2 = float(self.m_stk.pop())
        strOperation = self.m_stk.pop()
        dOperand1 = float(self.m_stk.pop())
        dResult = 0

        if strOperation == "+":
            dResult = dOperand1 + dOperand2
        elif strOperation == "-":
            dResult = dOperand1 - dOperand2
        elif strOperation == "/":
            dResult = dOperand1 / dOperand2
        elif strOperation == "*":
            dResult = dOperand1 * dOperand2

        self.m_plcd.display(dResult)

    def slotButtonClicked(self):
        button_text = self.sender().text()

        if button_text == "CE":
            self.m_stk.clear()
            self.m_strDisplay = ""
            self.m_plcd.display("0")
            return
        if any(char.isdigit() for char in button_text):
            self.m_strDisplay += button_text
            self.m_plcd.display(float(self.m_strDisplay))
        elif button_text == ".":
            self.m_strDisplay += button_text
            self.m_plcd.display(self.m_strDisplay)
        else:
            if len(self.m_stk) >= 2:
                self.m_stk.append(str(self.m_plcd.value()))
                self.calculate()
                self.m_stk.clear()
                self.m_stk.append(str(self.m_plcd.value()))
                if button_text != "=":
                    self.m_stk.append(button_text)
            else:
                self.m_stk.append(str(self.m_plcd.value()))
                self.m_stk.append(button_text)

                self.m_strDisplay = ""
                self.m_plcd.display("0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.setWindowTitle("Calculator")

    sys.exit(app.exec())
