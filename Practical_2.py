import turtle

t = turtle.Turtle()

def setup_axes():
    t.penup()
    t.goto(-400, 0)
    t.pendown()

    t.forward(800)

    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.setheading(90)
    t.forward(300)

    t.penup()
    t.goto(420, 0)
    t.pendown()
    t.write("x")

    t.penup()
    t.goto(0, 220)
    t.pendown()
    t.write("y")

def plot_function():
    screen = turtle.Screen()
    screen.setup(800, 400)
    screen.setworldcoordinates(-400, -100, 400, 200)

    setup_axes()

    t.penup()
    t.goto(-400, 0)

    for x in range(-400, 400):
        y = x / 3 + 5
        t.goto(x, y)
        t.pendown()

    screen.exitonclick()

plot_function()