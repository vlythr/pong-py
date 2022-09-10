import turtle
import os

wd = turtle.Screen()
wd.title("Pong by @vlythr")
wd.bgcolor("purple")
wd.setup(width=800, height=600)
wd.tracer(0)

# Score
score_a = 0
score_b = 0

# Right Paddle
right_p = turtle.Turtle()
right_p.speed(0)
right_p.shape("square")
right_p.color("green")
right_p.shapesize(stretch_wid=5, stretch_len=1)
right_p.penup()
right_p.goto(-350, 0)

# Left Paddle
left_p = turtle.Turtle()
left_p.speed(0)
left_p.shape("square")
left_p.color("green")
left_p.shapesize(stretch_wid=5, stretch_len=1)
left_p.penup()
left_p.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# Score Board
sb = turtle.Turtle()
sb.speed(0)
sb.color("green") 
sb.penup()
sb.hideturtle()
sb.goto(0, 260)
sb.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

# Function 
def right_p_up():
    y = right_p.ycor()
    y += 20
    right_p.sety(y)

def right_p_down():
    y = right_p.ycor()
    y -= 20
    right_p.sety(y)

def left_p_up():
    y = left_p.ycor()
    y += 20
    left_p.sety(y)

def left_p_down():
    y = left_p.ycor()
    y -= 20
    left_p.sety(y)

# Keyboard binding
wd.listen()
wd.onkeypress(right_p_up, "w")
wd.onkeypress(right_p_down, "s")

wd.listen()
wd.onkeypress(left_p_up, "Up")
wd.onkeypress(left_p_down, "Down")

# Main game loop
while True:
    wd.update()
    
    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)    

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        sb.clear()
        sb.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        os.system("aplay error.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        sb.clear()
        sb.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        os.system("aplay error.wav&")

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < left_p.ycor() + 40 and ball.ycor() > left_p.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < right_p.ycor() + 40 and ball.ycor() > right_p.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")