import turtle
import os

wd = turtle.Screen()
wd.title("Pong by @vlythr")
wd.bgcolor("purple")
wd.setup(width=800, height=600)
wd.tracer(0)

# Right Paddle
right_p = turtle.Turtle()
right_p.speed(0)
right_p.shape("square")
right_p.color("green")
right_p.penup()
right_p.goto(-350, 0)

# Left Paddle
left_p = turtle.Turtle()
left_p.speed(0)
left_p.shape("square")
left_p.color("green")
left_p.penup()
left_p.goto(350, 0)


# Main game loop
while True:
    wd.update()
    



