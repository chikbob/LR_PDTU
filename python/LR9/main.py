# Імпортуємо бібліотеку graphics
from graphics import *

win = GraphWin("Банка", 700, 700)

etiketka = [
    Polygon
    (Point(200, 500),

     Point(200, 200),
     Point(235, 215),
     Point(280, 230),
     Point(300, 235),
     Point(350, 240),
     Point(400, 235),
     Point(420, 230),
     Point(465, 215),
     Point(500, 200),

     Point(500, 500),
     Point(200, 500),
     )
]

bottom = [
    Polygon(
        Point(200, 500),
        Point(210, 510),
        Point(230, 520),
        Point(250, 530),
        Point(270, 540),

        Point(430, 540),
        Point(450, 530),
        Point(470, 520),
        Point(490, 510),
        Point(500, 500),
    )
]

top = [
    Oval(
        Point(275, 130),
        Point(425, 150)
    ),
    Line(Point(200, 200), Point(275, 140)),
    Line(Point(500, 200), Point(425, 140)),
]


def draw_lines():
    for line in etiketka:
        line.setFill("#d8d074")
        line.draw(win)
    for line in bottom:
        line.draw(win)
    for line in top:
        line.draw(win)


draw_lines()

msg = Text(Point(350, 600), "Банка")
msg.setSize(20)
msg.setTextColor("black")
msg.setStyle("bold")
msg.draw(win)

win.getMouse()  # чекаємо натискання кнопки миші
win.close()  # закриваємо вікно для графіки
