import turtle

wn = turtle.Screen()

t = turtle.Turtle()

t.shape('turtle')

length = 10
for _ in range(45):
    t.forward(length)
    t.right(90)
    length += 5

wn.exitonclick()
