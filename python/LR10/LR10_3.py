import turtle

wn = turtle.Screen()

for x in range(12):
    t = turtle.Turtle()
    t.shape('turtle')
    t.width(2)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(30 + x * 30)
    t.forward(100)

wn.exitonclick()