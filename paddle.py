from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid = 5, stretch_len = 1)
        self.goto(position)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
