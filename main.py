import time
from turtle import Screen, Turtle, xcor
from paddle import Paddle
from scoreboard import Score
from ball import Ball

screen = Screen()
screen.setup(height = 600, width = 800)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

userbet = screen.textinput( title = "Press any key to start : " , prompt = "Any key : ")


screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
scoreboard = Score()

game = True
x = 0.1
while game:
    time.sleep(x)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        x *= 0.9

    if ball.xcor() < -380 :
        ball.reset_position()
        scoreboard.right_point()
        x = 0.1

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        x = 0.1


screen.exitonclick()
