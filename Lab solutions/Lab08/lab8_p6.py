import turtle

def drawSquare(myturtle, x, y, a):
    """
    Draw a square
    :param myturtle: Get the turtle object
    :param x: Location
    :param y: Location
    :param a: Distance of movement
    :return: Void
    """
    myturtle.penup()
    myturtle.setposition(x, y)
    myturtle.pendown()
    for angle in [0, 90, 180, 270]:
        # Turn and move, 4 times
        myturtle.setheading(angle)
        myturtle.forward(a)
    myturtle.penup()

    #
    # Test code
    #
    # turtle.setup(800, 600)
    # window = turtle.Screen()
    # the_turtle = turtle.getturtle()
    # the_turtle.hideturtle()
    # drawSquare(the_turtle, 0, 0, 20)
    # drawSquare(the_turtle, -30, -30, 40)
    # window.exitonclick()
    #
