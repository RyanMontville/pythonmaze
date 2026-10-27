
import turtle
import random

class MazeTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("black")

    def go_to_top_left(self):
        self.pu()
        self.goto(-390, 290)
        self.pd()

    def draw_border(self):
        self.go_to_top_left()
        for i in range(2):
            self.forward(780)
            self.right(90)
            self.forward(560)
            self.pu()
            self.forward(20)
            self.pd()
            self.right(90)

    def draw_vertical(self, xcoord):
        self.pu()
        self.goto(xcoord, 290)
        self.setheading(270)
        while self.ycor() > -290:
            if random.choice([True, False]):
                self.pd()
            else:
                self.pu()
            self.forward(20)

    def draw_horizontal(self, ycoord):
        self.pu()
        self.goto(-390, ycoord)
        self.setheading(0)
        while self.xcor() < 390:
            if random.choice([True, False]):
                self.pd()
            else:
                self.pu()
            self.forward(20)

    def draw_all_vertical(self):
        x_index = -370
        for i in range(38):
            self.draw_vertical(x_index)
            x_index += 20

    def draw_all_horizontal(self):
        y_index = 270
        for i in range(28):
            self.draw_horizontal(y_index)
            y_index -= 20

screen = turtle.Screen()
screen.bgcolor("white")

maze_drawer = MazeTurtle()
maze_drawer.draw_border()
maze_drawer.draw_all_vertical()
maze_drawer.draw_all_horizontal()

turtle.done()