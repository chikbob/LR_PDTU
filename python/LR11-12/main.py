import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

param1 = simpledialog.askfloat("Sin", "Введіть параметр функції sin:")
param2 = simpledialog.askfloat("Cos", "Введіть параметр функції cos:")
param3 = simpledialog.askfloat("Tg", "Введіть параметр функції tg:")

x = np.linspace(-10, 10, 100)
y1 = np.sin(param1 * x)
y2 = np.cos(param2 * x)
y3 = np.tan(param3 * x)

plt.figure()
plt.plot(x, y1, label='sin({}x)'.format(param1))
plt.plot(x, y2, label='cos({}x)'.format(param2))
plt.plot(x, y3, label='tg({}x)'.format(param3))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функцій')
plt.legend()
plt.show()