from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

# Gameboard
screen = Screen()
screen.bgcolor("black")
screen.reset()
screen.setup(1000, 600)
screen.title("Pong")
screen.tracer(0)

# border
positions = [(0,-270), (0, -210), (0,-150), (0, -90), (0, -30), (0, 30), (0,90), (0, 150), (0,210), (0,270)]
border = []

for i in range(len(positions)):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.resizemode("user")
    new_turtle.shapesize(2, 1)
    new_turtle.goto(positions[i])
    border.append(new_turtle)

# Paddle and ball
left_paddle = Paddle((-460, 0))
right_paddle = Paddle((460, 0))
ball = Ball()
score = Score()

# up-down
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 430) or (ball.distance(left_paddle) < 50 and ball.xcor() < -430):
        ball.bounce_x()

    if ball.xcor() > 470:
        ball.center()
        score.left_score()

    if ball.xcor() < -470:
        ball.center()
        score.right_score()

screen.exitonclick()
