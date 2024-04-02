from turtle import Turtle
import random

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        # starts with coordinates to draw the border of the maze
        self.draw_from_array([(-390,290,390,290),(390,290,390,-270),(390,-290,-390,-290),(-390,-290,-390,270)])
        self.hideturtle()
        self.speed("fastest")
        
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
            
        # If the height of the vertical zig zags is 120, the program can choose to add a spiral before drawing the horizontal zig zags
        draw_spiral = False
        if choice[0] == 120:
            if random.choice([True, False]):
                draw_spiral = True
                end_of_spiral = self.draw_spiral(right_edge_of_vertical_zig_zag,y_coordinate)
                self.draw_line_from_tuple((right_edge_of_vertical_zig_zag,(y_coordinate-140),(right_edge_of_vertical_zig_zag+120),(y_coordinate-140)))
                right_edge_of_vertical_zig_zag = end_of_spiral[0]
        
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
        return (bottom_of_zig_zags, draw_spiral)
    
    def update_coordinates(self,x_coordinate,y_coordinate,x_start_change,x_end_change,y_start_change,y_end_change):
        x_start = x_coordinate + x_start_change
        x_end = x_coordinate + x_end_change
        y_start = y_coordinate + y_start_change
        y_end = y_coordinate + y_end_change
        self.draw_line_from_tuple((x_start,y_start,x_end,y_end))
        return (x_end,y_end)
            
    def draw_spiral(self, x_coordinate, y_coordinate):
        # Draw outside bottom of spiral
        coords = self.update_coordinates(x_coordinate,y_coordinate,0,120,-120,-120)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        # Draw left
        coords = self.update_coordinates(coords[0],coords[1],0,-80,0,0)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-60)
        # Draw right
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        # Draw the spiral going back out, starting with up
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,0,20)
        # Draw right
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-60)
        # Draw left
        coords = self.update_coordinates(coords[0],coords[1],0,-80,0,0)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        return (x_coordinate+120,y_coordinate)
    
    def draw_multipath_variation_one(self,x_coordinate,y_coordinate):
        # Draw 1st path, starting with right
        coords = self.update_coordinates(x_coordinate,y_coordinate,20,400,-120,-120)
        # Draw right edge
        self.update_coordinates(coords[0],coords[1],20,20,-20,120)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        # Draw left
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-80)
        # Draw left
        coords = self.update_coordinates(coords[0],coords[1],0,-360,0,0)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,80)
        # Draw 2nd path, starting with down
        coords = self.update_coordinates(coords[0],coords[1],20,20,0,-60)
        # Draw right
        coords = self.update_coordinates(coords[0],coords[1],0,200,0,0)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        # Draw 3rd path, starting with down
        coords = self.update_coordinates(x_coordinate,y_coordinate,60,60,-20,-60)
        # Draw right
        coords = self.update_coordinates(coords[0],coords[1],0,220,0,0)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,0,-20)
        # Draw right
        coords = self.update_coordinates(coords[0],coords[1],0,100,0,0)
        # Draw left
        coords = self.update_coordinates(coords[0],coords[1],20,-60,20,20)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,40)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],20,20,20,-20)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],20,20,-20,20)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],20,20,20,-20)
        # Draw 4th path, starting with up
        coords = self.update_coordinates(coords[0],coords[1],-80,-80,-20,40)
        # Draw left
        coords = self.update_coordinates(coords[0],coords[1],0,-180,-20,-20)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,20,-20)
        # Draw right
        coords = self.update_coordinates(coords[0],coords[1],0,180,0,0)
        return (x_coordinate+420,y_coordinate)
    
    def draw_multipath_variation_two(self,x_coordinate,y_coordinate):
        # this multipath is drawn out of order, so it is hard to comment what is happening
        coords = self.update_coordinates(x_coordinate,y_coordinate,220,220,0,-20)
        for i in range(3):
            coords = self.update_coordinates(coords[0],coords[1],-40,-40,20,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,-80,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        self.update_coordinates(coords[0],coords[1],20,20,0,20)
        coords = self.update_coordinates(coords[0],coords[1],20,40,0,0)
        self.update_coordinates(coords[0],coords[1],20,20,0,20)
        self.update_coordinates(coords[0],coords[1],60,60,0,20)
        self.update_coordinates(coords[0],coords[1],100,100,0,20)
        coords = self.update_coordinates(coords[0],coords[1],20,120,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,0)
        self.update_coordinates(coords[0],coords[1],20,20,20,60)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,40)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,20,-60)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,0,60)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,20,-40)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,60,0)
        coords = self.update_coordinates(coords[0],coords[1],0,-100,40,40)
        coords = self.update_coordinates(coords[0],coords[1],80,80,-60,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,-60,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,40,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-40,180,-20,-20)
        return coords[1]-20
        
    def fill_rest_of_row(self,y_coordinate):
        coords = self.update_coordinates(390,y_coordinate,-20,-20,-20,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,-80,0,0)
        self.update_coordinates(coords[0],coords[1],-20,-20,-20,80)
        self.update_coordinates(coords[0],coords[1],-20,100,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-20,60,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,40)
        self.update_coordinates(coords[0],coords[1],20,-60,20,20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,20,20,20)
        self.update_coordinates(coords[0],coords[1],-20,-20,20,40)
        
    def draw_second_row(self,x_coordinate,y_coordinate,has_spiral_been_drawn):
        bottom_line = 0
        if has_spiral_been_drawn:
            end_coord = self.draw_multipath_variation_one(x_coordinate,y_coordinate)
            bottom_line = self.draw_multipath_variation_two(end_coord[0],end_coord[1])
            self.fill_rest_of_row(y_coordinate)
        else:
            end_coord = self.draw_spiral(x_coordinate,y_coordinate)
            second_end_coord = self.draw_multipath_variation_one(end_coord[0],end_coord[1])
            bottom_line = self.draw_multipath_variation_two(second_end_coord[0],second_end_coord[1])
        return bottom_line
    
    def draw_stair_paths(self,x_coordinate,y_coordinate):
        # Draw top line
        coords = self.update_coordinates(x_coordinate,y_coordinate,0,120,0,0)
        # Draw right side of stairs section
        self.update_coordinates(coords[0],coords[1],20,20,20,-160)
        #randomly make either the right side or bottom of section a dead end
        bottom_path_dead_end = random.choice([True,False])
        if bottom_path_dead_end:
            temp_coords = coords
            temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],0,0,0,-160)
            self.update_coordinates(temp_coords[0],temp_coords[1],-120,40,-20,-20)
        else:
            temp_coords = coords
            temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],0,0,0,-180)
            temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],-120,-40,0,0)
            self.update_coordinates(temp_coords[0],temp_coords[1],20,80,0,0)
        # Draw top left curl
        coords = self.update_coordinates(coords[0],coords[1],-120,-80,-40,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        # Draw top right group
        coords = self.update_coordinates(coords[0],coords[1],40,80,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,20,40,40)
        coords = self.update_coordinates(coords[0],coords[1],0,20,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-40,-20,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],20,20,80,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        # Draw right side of stairs
        coords = self.update_coordinates(coords[0],coords[1],40,20,-40,-40)
        for i in range(3):
            coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
            coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        # Draw left side of stairs
        coords = self.update_coordinates(coords[0],coords[1],0,-20,20,20)
        temp_coords = self.update_coordinates(coords[0],coords[1],0,0,0,-100)
        self.update_coordinates(temp_coords[0],temp_coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,20,-60,-60)
        for i in range(2):
            coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
            coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        
    def draw_third_row(self,top_coordinate):
        self.draw_stair_paths(-390,top_coordinate)