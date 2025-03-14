import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('#262626')
t.pencolor('black')
t.speed(100)

col = ('red', 'yellow', 'orange', 'green')

for n in range(10):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(1)
            t.circle(80+n*20, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()
turtle.done()
