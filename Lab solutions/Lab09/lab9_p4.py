def drawFlower(myturtle, r):
    """
    Drawing flower with circles
    :param myturtle: given turtle object
    :param r: given int
    :return: none
    """
    # Set position, color
    myturtle.setposition(0, 0)
    myturtle.pencolor('red')
    myturtle.pendown()
    for a in range(0, 360, 15):
        myturtle.setheading(a)
        myturtle.circle(r)
    # angle = 0
    # while angle < 360:
    #     myturtle.setheading(angle)
    #
    #     myturtle.circle(r)
    #
    #     angle += 360 // 24
    myturtle.penup()

    # Test code

    #
    # import turtle
    #
    # turtle.setup(600, 600)
    # mywindow = turtle.Screen()
    #
    # myturtle = turtle.getturtle()
    #
    # flag = int(input('r = '))
    # while flag:
    #     drawFlower(myturtle, flag)
    #     flag = int(input('r = '))
    #
