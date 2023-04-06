from turtle import Turtle, xcor

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.dir = 1
        self.pdir = 1

    def move(self):
        newx = self.xcor() + 10 * self.pdir
        newy = self.ycor() + 10 * self.dir
        self.goto(newx, newy)

    def bounce(self):
        self.dir *= -1

    def paddle_bounce(self):
        self.pdir *= -1

    def reset_position(self):
        self.goto(0,0)
        self.pdir *= -1

