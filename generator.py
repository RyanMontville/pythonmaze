from turtle import Turtle
import random

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        # starts with coordinates to draw the border of the maze
        self.coordinate_array = []
        self.draw_from_array([(-390,290,390,290),(390,290,390,-270),(390,-290,-390,-290),(-390,-290,-390,270)])
        self.hideturtle()
        
    def print_cors(self):
        xint = int(self.xcor())
        yint = int(self.ycor())
        print("X: " + str(xint) + ", Y: " + str(yint))
    
    def draw_from_array(self, array):
        for i in array:
            self.coordinate_array.append(i)
            self.draw_line_from_tuple(i)
            
    
    def draw_line_from_tuple(self,ct):
        self.pu()
        self.goto(ct[0],ct[1])
        self.pd()
        self.goto(ct[2],ct[3])
        
            
    def return_possible_directions(self):
        directions = ["left","right","up","down"]
        if self.ycor() <= -290:
            directions.remove("down")
        if self.ycor() >= 290:
            directions.remove("up")
        if self.xcor() <= -390:
            directions.remove("left")
        if self.xcor() >= 390:
            directions.remove("right")
        return directions
    
    def check_for_collision(self,xcoord,ycoord):
        x_collision = False
        y_collision = False
        for i in self.coordinate_array:
            if i[0] < i[2]:
                if xcoord >= i[0]:
                    if xcoord <= i[2]:
                        x_collision = True
                        break
            else:
                if xcoord >= i[2]:
                    if xcoord <= i[0]:
                        x_collision = True
                        break
            if i[1] > i[3]:
                if ycoord >= i[1]:
                    if ycoord <= i[3]:
                        y_collision = True
                        break
            else:
                if ycoord >= i[3]:
                    if ycoord <= i[1]:
                        y_collision = True
                        break
        if x_collision:
            if y_collision:
                return True
        return False