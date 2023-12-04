import turtle

t = turtle.Turtle()
t.shape('turtle')

colors = ['red', 'orange', 'green', 'blue', 'purple']

for x in range(5):
    t.color(colors[x])
    t.penup()
    t.goto(0, -x * 10)
    t.pendown()
    t.circle(50 + x * 10)

turtle.exitonclick()