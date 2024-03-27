from turtle import Turtle
import random

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        
    def go_to_top_left(self):
        self.pu()
        self.goto(-390,290)
        self.pd()
        
    def draw_border(self):
        self.go_to_top_left()
        for i in range(2):
            self.forward(780)
            self.print_cors()
            self.right(90)
            self.forward(560)
            self.print_cors()
            self.pu()
            self.forward(20)
            self.pd()
            self.right(90)
            
    def draw_vertical(self):
        while(self.ycor() == range(0,5)):
            print("hello")
            
    def print_cors(self):
        xint = int(self.xcor())
        yint = int(self.ycor())
        print("X: " + str(xint) + ", Y: " + str(yint))
        
    def draw_line(self, direction, coordinate):
        if direction == "right":
            heading = 0
            x_cord = -390
            y_cord = coordinate
            travel_distance = 780
        elif direction == "left":
            heading = 180
            x_cord = 390
            y_cord = coordinate
            travel_distance = 780
        elif direction == "up":
            heading = 90
            x_cord = coordinate
            y_cord = -290
            travel_distance = 580
        else:
            heading = 270
            x_cord = coordinate
            y_cord = 290
            travel_distance = 580
        self.setheading(heading)
        self.pu()
        self.goto(x_cord, y_cord)
        self.pd()
        self.forward(travel_distance)