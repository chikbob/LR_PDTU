import turtle

wn = turtle.Screen()

t = turtle.Turtle()
t.speed(0)

t.penup()
t.circle(90, 90)
t.pendown()

for x in range(6):
    t.circle(50+x*10, 360)
    t.penup()
    t.pendown()
for x in range(6):
    t.circle(-50-x*10, 360)
    t.penup()
    t.pendown()

wn.exitonclick()