import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')

len = 160
for _ in range(9):
    t.forward(300)
    t.right(len)

wn.exitonclick()