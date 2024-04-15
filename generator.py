from turtle import Turtle
import random

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_border()
        self.hideturtle()
        self.speed("fastest")
        
    def print_cors(self):
        xint = int(self.xcor())
        yint = int(self.ycor())
        print("X: " + str(xint) + ", Y: " + str(yint))
        
    def draw_line_from_tuple(self,ct):
        self.pu()
        self.goto(ct[0],ct[1])
        self.pd()
        self.goto(ct[2],ct[3])
        
    def update_coordinates(self,x_coordinate,y_coordinate,x_start_change,x_end_change,y_start_change,y_end_change):
        x_start = x_coordinate + x_start_change
        x_end = x_coordinate + x_end_change
        y_start = y_coordinate + y_start_change
        y_end = y_coordinate + y_end_change
        self.draw_line_from_tuple((x_start,y_start,x_end,y_end))
        return (x_end,y_end)
        
    def update_coordinates_from_array(self,st_coords,coords_array):
        coordinates = self.update_coordinates(st_coords[0],st_coords[1],st_coords[2],st_coords[3],st_coords[4],st_coords[5])
        for ct in coords_array:
            coordinates = self.update_coordinates(coordinates[0],coordinates[1],ct[0],ct[1],ct[2],ct[3])
        return coordinates
            
    def draw_border(self):      
        border_start = (-390,290,0,780,0,0)
        border_array = [(0,0,0,-560),(0,-780,-20,-20),(0,0,0,560)]
        self.update_coordinates_from_array(border_start,border_array)
        
    def draw_grid(self):
        self.pencolor("LightGrey")
        coords = self.update_coordinates(-390,270,0,780,0,0)
        while coords[1] > -270:
            coords = self.update_coordinates(-390,coords[1],0,780,-20,-20)
        coords = self.update_coordinates(-370,290,0,0,0,-580)
        while coords[0] < 370:
            coords = self.update_coordinates(coords[0],290,20,20,0,-580)
        self.pencolor("black")

    def draw_a(self,start_x, start_y,top_or_bottom):
        #Draw the A
        self.pensize(2)
        start_coords = (start_x,start_y,40,70,-180,-40)
        coords_array = [(20,50,0,-140),(-20,-30,0,60),(0,-20,0,0),(0,-10,0,-60),(10,15,80,110),(0,10,0,0),
                        (0,5,0,-30),(0,-20,0,0)]
        self.update_coordinates_from_array(start_coords,coords_array)
        self.pensize(1)
        #Draw left side, from top to bottom
        start_coords = (start_x,start_y,20,20,0,-40)
        coords_array = [(-20,20,-20,-20),(0,0,0,40),(0,20,0,0),(20,20,20,0),(-20,-60,-60,-60),(-20,20,-20,-20),
                        (0,0,0,-20),(-20,-20,0,-20),(0,30,0,0),(-50,-30,-20,-20),(0,20,-20,-20),(20,20,0,-20),
                        (0,-60,0,0),(80,80,60,-20),(0,-60,0,0),(-20,120,-20,-20),(-40,-40,0,20),(-20,20,20,20),
                        (0,0,-20,60),(0,20,20,20),(-36,-20,20,20),(0,0,0,20),(20,0,20,20),(-20,0,20,20),(0,0,0,20),
                        (-20,-20,-60,0)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        #Close off paths based on wether you enter from the top or bottom
        if top_or_bottom == "top":
            close_coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
            #close off either top of A or bottom left of A
            self.pensize(2)
            if random.choice([True, False]):
                self.update_coordinates(close_coords[0],close_coords[1],-10,10,-20,-20)
            else:
                self.update_coordinates(close_coords[0],close_coords[1],-20,-40,-160,-160)
            self.pensize(1)
        else:
            self.pensize(2)
            close_coords = self.update_coordinates(start_x,start_y,70,90,-40,-40)
            self.pensize(1)
            close_coords = self.update_coordinates(close_coords[0],close_coords[1],-10,-10,-180,-200)
        #close off top or bottom exit
        if random.choice([True, False]):
            # Exit on top
            self.update_coordinates(coords[0],coords[1],40,40,0,-220)
            return (start_x + 140, start_y,"top")
        else:
            self.update_coordinates(coords[0],coords[1],40,40,20,-200)
            return (start_x + 140, start_y,"bottom")
        
    def draw_b(self,start_x, start_y,top_or_bottom):
        self.pensize(2)
        coords = self.update_coordinates(start_x,start_y,40,40,-160,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,40,20,20)
        coords = self.update_coordinates(coords[0],coords[1],-40,0,-140,-140)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,120,80)
        coords = self.update_coordinates(coords[0],coords[1],0,0,-20,-60)
        coords = self.update_coordinates(coords[0],coords[1],20,20,-20,-20)
        self.setheading(0)
        self.circle(35, 180)
        self.setheading(0)
        self.circle(35, 180)
        coords = self.update_coordinates(self.xcor(),self.ycor(),-20,-20,-120,-120)
        self.setheading(0)
        self.circle(20, 180)
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,0,20,20)
        self.setheading(0)
        self.circle(20, 180)