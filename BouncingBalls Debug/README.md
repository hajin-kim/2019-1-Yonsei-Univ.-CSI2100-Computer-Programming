BouncingBalls_SimplyDebugged
2019년 5월 9일, 목요일, 오후 3:05 에 김하진 씀

We can find a bug that a ball sometimes moves zig-zag or be disappeared, at lab8_p5 BouncingBalls.

 

This problem can be simply debugged by following process.

line 87; elif ......

Change this into

line 87; if ......

 

Let's see wide view

if atLeftEdge(balls[k], screen_width):
    balls[k].setheading(bounceBall(balls[k],'right'))
elif atRightEdge(balls[k], screen_width):
    balls[k].setheading(bounceBall(balls[k],'left'))
elif atTopEdge(balls[k], screen_height):
    balls[k].setheading(bounceBall(balls[k],'down'))
elif atBottomEdge(balls[k], screen_height):
    balls[k].setheading(bounceBall(balls[k],'up'))
Change this into

if atLeftEdge(balls[k], screen_width):
    balls[k].setheading(bounceBall(balls[k],'right'))
elif atRightEdge(balls[k], screen_width):
    balls[k].setheading(bounceBall(balls[k],'left'))
if atTopEdge(balls[k], screen_height):
    balls[k].setheading(bounceBall(balls[k],'down'))
elif atBottomEdge(balls[k], screen_height):
    balls[k].setheading(bounceBall(balls[k],'up'))
 

The bug caused when a ball moves over two edges.(for example, over both right side and top side)

In this situation, previous if statement is if-elif-elif-elif so setheading is executed only once.

Following changing, in this situation, now if-elif if-elif makes setheading like this:

 1;   Angle

 2;   once if;  180-Angle

 3;   next if;   360-(180-Angle) = 180+Angle

So the ball moves back and zig-zag problem isn't occured.