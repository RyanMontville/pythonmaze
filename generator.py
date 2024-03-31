from turtle import Turtle
import random

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        # starts with coordinates to draw the border of the maze
        self.draw_from_array([(-390,290,390,290),(390,290,390,-270),(390,-290,-390,-290),(-390,-290,-390,270)])
        self.hideturtle()
        
    def print_cors(self):
        xint = int(self.xcor())
        yint = int(self.ycor())
        print("X: " + str(xint) + ", Y: " + str(yint))
    
    def draw_from_array(self, array):
        for i in array:
            self.draw_line_from_tuple(i)
    
    def draw_line_from_tuple(self,ct):
        self.pu()
        self.goto(ct[0],ct[1])
        self.pd()
        self.goto(ct[2],ct[3])
        
    def draw_zig_zags(self, x_coordinate, y_coordinate):
        # randomly choose how long the vertical zig zags will be
        random_lengths = [(60,"even"),(80,"odd"),(100,"both"),(120,"both")]
        choice = random.choice(random_lengths)
        end_of_zig = y_coordinate - choice[0]
        bottom_of_zig_zags = end_of_zig-20
        # randomly choose how many vertical zig zags there will be
        range_options = []
        if choice[1] == "even":
            range_options = [6,8,10,12,14]
        elif choice[1] == "odd":
            range_options = [5,7,9,11,13,15]
        elif choice[1] == "both":
            range_options = [5,6,7,8,9,10,11,12,13,14,15]
        # keep track of number of zig zags
        total = 0
        # start drawing the vertical zig zags
        for i in range(random.choice(range_options)):
            vertical_offset = (x_coordinate + 20) + (i * 20)
            # draw down (zig)
            if i % 2 == 0:
                self.draw_line_from_tuple((vertical_offset,y_coordinate,vertical_offset,end_of_zig))
            # draw up (zag)
            else:
                self.draw_line_from_tuple((vertical_offset,bottom_of_zig_zags,vertical_offset,(y_coordinate-20)))
            total += 1
        right_edge_of_vertical_zig_zag = x_coordinate + (total * 20)
        # need to draw a line under the zig zags in some cases to make the path end at the correct locations
        manual_line = False
        if choice[0] == 60 or choice[0] == 100:
            if total % 2 == 0:
                manual_line = True
        # draw the bottom line(s) of the zig zags
        if manual_line:
            self.draw_line_from_tuple(((x_coordinate),bottom_of_zig_zags,right_edge_of_vertical_zig_zag,bottom_of_zig_zags))
            bottom_of_zig_zags -= 20
            self.draw_line_from_tuple(((x_coordinate + 20),bottom_of_zig_zags,370,bottom_of_zig_zags))
        else:
            self.draw_line_from_tuple(((x_coordinate + 20),bottom_of_zig_zags,right_edge_of_vertical_zig_zag,bottom_of_zig_zags))
        # start of horizontal zig zags
        start_of_zig = right_edge_of_vertical_zig_zag
        start_of_zag = right_edge_of_vertical_zig_zag + 20
        horizontal_offset = 0
        # zig zags drawn from bottom to top
        if total % 2 == 0:
            horizontal_offset = (y_coordinate-20)
            horizontal_count = 0
            while horizontal_offset > (bottom_of_zig_zags-20):
                # draw right (zig)
                if horizontal_count % 2 == 0:
                    self.draw_line_from_tuple((start_of_zig,horizontal_offset,370,horizontal_offset))
                    horizontal_offset -= 20
                    horizontal_count += 1
                # draw left (zag)
                else:
                    self.draw_line_from_tuple((390,horizontal_offset,start_of_zag,horizontal_offset))
                    horizontal_offset -= 20
                    horizontal_count += 1
        # zig zags drawn from top to bottom
        else:
            horizontal_offset = bottom_of_zig_zags
            horizontal_count = 0
            self.draw_line_from_tuple((vertical_offset,horizontal_offset,370,horizontal_offset))
            horizontal_offset += 20
            while horizontal_offset < y_coordinate:
                # draw right (zig)
                if horizontal_count % 2 == 0:
                    self.draw_line_from_tuple((start_of_zig,horizontal_offset,350,horizontal_offset))
                    horizontal_offset += 20
                    horizontal_count += 1
                # draw left (zag)
                else:
                    self.draw_line_from_tuple((370,horizontal_offset,start_of_zag,horizontal_offset))
                    horizontal_offset += 20
                    horizontal_count += 1
            # draw a line for the path on the far right side to get from top right corner to bottom of horizontal zig zags
            self.draw_line_from_tuple((370,(y_coordinate-20),370,bottom_of_zig_zags))