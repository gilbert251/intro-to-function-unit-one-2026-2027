import turtle

t = turtle.Turtle()
t.shape('turtle')
t.speed(3)  # Set drawing speed


TURN_ANGLE = 45


def burger(wow):
    print(wow)


def octagon(side_length):
    for _ in range(8):
        t.forward(side_length)
        t.left(TURN_ANGLE)

burger("Drawing a octagon...")
octagon(100)

t.penup()
t.goto(150, 0)  
t.pendown()




turtle.done()
