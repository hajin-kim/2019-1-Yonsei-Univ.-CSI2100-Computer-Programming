import turtle

# Settings
turtle.setup(600, 600)

window = turtle.Screen()

the_turtle = turtle.getturtle()
the_turtle.hideturtle()

# Draw an X
the_turtle.penup()
the_turtle.setposition(-300, 300)
the_turtle.pendown()
the_turtle.setposition(300, -300)
the_turtle.penup()
the_turtle.setposition(300, 300)
the_turtle.pendown()
the_turtle.setposition(-300, -300)

window.exitonclick()
