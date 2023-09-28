import turtle

def draw_star(n, size):
    if n % 2 == 0:
        print("Point count must be an odd number!")
        return
    
    angle = 360 / n
    for _ in range(n):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.left(2 * angle)

draw_star(7, 75)

turtle.penup() # start drawing 2nd star under 1st
turtle.goto(0, -200)
turtle.pendown()

draw_star(5, 75)
turtle.done()