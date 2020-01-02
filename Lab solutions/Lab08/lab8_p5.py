# Bouncing Balls Simulation Program

import turtle
import random
import time


def colorChange(colors):
    """
    For change colors
    :param colors: Use its aliasing
    :return: [r, g, b]
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    #
    # Test code
    #
    # r = 0
    # g = 0
    # b = random.randint(0, 1) * 255
    #

    if [r, g, b] == colors:
        return colorChange(colors)
    else:
        return [r, g, b]


def atLeftEdge(ball, screen_width):
    """
    These functions will find if the ball is over the edge or not
    :param ball: Chosen ball
    :param screen_width: Width of screen
    :return: Boolean True of False
    """
    if ball.xcor() < -screen_width / 2:
        return True # Return Boolean True
    else:
        return False


def atRightEdge(ball, screen_width):
    """
    These functions will find if the ball is over the edge or not
    :param ball: Chosen ball
    :param screen_width: Width of screen
    :return: Boolean True of False
    """
    if ball.xcor() > screen_width / 2:
        return True # Return Boolean True
    else:
        return False


def atTopEdge(ball, screen_height):
    """
    These functions will find if the ball is over the edge or not
    :param ball: Chosen ball
    :param screen_width: height of screen
    :return: Boolean True of False
    """
    if ball.ycor() > screen_height / 2:
        return True # Return Boolean True
    else:
        return False


def atBottomEdge(ball, screen_height):
    """
    These functions will find if the ball is over the edge or not
    :param ball: Chosen ball
    :param screen_width: height of screen
    :return: Boolean True of False
    """
    if ball.ycor() < -screen_height / 2:
        return True # Return Boolean True
    else:
        return False


def bounceBall(ball, new_direction, colors):
    """
    Several lines of codes are newly added
    :param ball: Chosen ball
    :param new_direction: Related to direction of leached edge
    :param colors: Use its aliasing
    :return: New direction of the ball
    """
    if new_direction == 'left' or new_direction == 'right':
        new_heading = 180 - ball.heading()
    elif new_direction == 'down' or new_direction == 'up':
        new_heading = 360 - ball.heading()

    # When ball is bounced, change its color and previously used color value
    new_color = colorChange(colors)
    colors[0] = new_color[0]
    colors[1] = new_color[1]
    colors[2] = new_color[2]
    turtle.colormode(255)
    ball.fillcolor(colors[0], colors[1], colors[2])

    return new_heading


def createBalls(num_balls):
    """
    Creating balls
    :param num_balls: The nubmer of balls
    :return: Balls in list
    """
    balls = []
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        new_ball.fillcolor('black')
        new_ball.speed(0)

        # Instead of using pendown()
        # new_ball.penup()

        new_ball.setheading(random.randint(1, 359))
        balls.append(new_ball)

    return balls


# ---- main
# program greeting
print('This program simulates bouncing balls in a turtle screen')
print('for a specified number of seconds.')

# init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width, screen_height)

# create turtle window
window = turtle.Screen()
window.title('Bouncing Balls')

# prompt user for execution time and number of balls
num_seconds = int(input('Enter number of seconds to run: '))
num_balls = int(input('Enter number of balls in simulation: '))

# create balls
balls = createBalls(num_balls)

# Create a list of previously used colors
colors_previously_used = []
for i in range(0, num_balls):
    colors_previously_used.append([0,0,0])

# set start time
start_time = time.time()

# begin simulation
terminate = False

while not terminate:
    for k in range(0, len(balls)):
        balls[k].forward(15)

        # 3 arguements are needed. Newly added
        if atLeftEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'right', colors_previously_used[k]))
        elif atRightEdge(balls[k], screen_width):
            balls[k].setheading(bounceBall(balls[k], 'left', colors_previously_used[k]))
        elif atTopEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'down', colors_previously_used[k]))
        elif atBottomEdge(balls[k], screen_height):
            balls[k].setheading(bounceBall(balls[k], 'up', colors_previously_used[k]))

        if time.time() - start_time > num_seconds:
            terminate = True

# exit on close window
turtle.exitonclick()
