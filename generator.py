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
        # choice = random.choice(random_lengths)
        choice = random_lengths[3]
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
            
        # If the height of the vertical zig zags is 120, draw the spiral on the 1st row instead of the second row
        draw_spiral = False
        if choice[0] == 120:
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
        self.update_coordinates(coords[0],coords[1],20,20,0,120)
        # Draw up
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        #randomly close one of the paths
        if random.choice([True,False]):
            self.update_coordinates(x_coordinate,y_coordinate,380,400,-20,-20)
        else:
            self.update_coordinates(x_coordinate,y_coordinate,380,380,-20,0)
        # Draw down
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,0,-80)
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
        # Randomly decide if bottom right corner should be a dead end
        if random.choice([True, False]):
            self.update_coordinates(x_coordinate,y_coordinate,400,420,-120,-120)
            return (x_coordinate+420,y_coordinate,True)
        else:
            return (x_coordinate+420,y_coordinate,False)
    
    def draw_multipath_variation_two(self,x_coordinate,y_coordinate,is_one_dead_end):
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
        if (is_one_dead_end == False):
            self.update_coordinates(x_coordinate,y_coordinate,0,20,-120,-120)
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
            bottom_line = self.draw_multipath_variation_two(end_coord[0],end_coord[1],end_coord[2])
            self.fill_rest_of_row(y_coordinate)
        else:
            end_coord = self.draw_spiral(x_coordinate,y_coordinate)
            second_end_coord = self.draw_multipath_variation_one(end_coord[0],end_coord[1])
            bottom_line = self.draw_multipath_variation_two(second_end_coord[0],second_end_coord[1],second_end_coord[2])
        return bottom_line
    
    def draw_stair_paths(self,x_coordinate,y_coordinate):
        # Draw top line
        coords = self.update_coordinates(x_coordinate,y_coordinate,0,120,0,0)
        # Draw right side of stairs section
        self.update_coordinates(coords[0],coords[1],20,20,20,-160)
        #randomly make either the right side or bottom of section a dead end
        bottom_path_dead_end = False
        right_side_closed = random.choice([True,False])
        if right_side_closed:
            temp_coords = coords
            # Draw the right side closed
            temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],0,0,0,-180)
            # Draw bottom line with a opening
            temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],-120,-40,0,0)
            self.update_coordinates(temp_coords[0],temp_coords[1],20,80,0,0)
        else:
            temp_coords = coords
            temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],0,0,0,-160)
            # Decide if bottom is a dead end or not
            bottom_path_dead_end = random.choice([True, False])
            if bottom_path_dead_end:
                # Draw bottom closed
                self.update_coordinates(temp_coords[0],temp_coords[1],-120,40,-20,-20)
            else:
                # Draw the bottom with an opening
                temp_coords = self.update_coordinates(temp_coords[0],temp_coords[1],-120,-60,-20,-20)
                self.update_coordinates(temp_coords[0],temp_coords[1],20,100,0,0)
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
        if (bottom_path_dead_end==False) and (right_side_closed==False):
            return False
        else:
            return True
        
    def draw_many_random_choices(self, top_coordinate, did_stairs_end):
        x_coordinate = -230
        # Draw left corner back abd forth
        coords = self.update_coordinates(x_coordinate, top_coordinate,180,0,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-180)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,140)
        coords = self.update_coordinates(coords[0],coords[1],0,140,0,0)
        coords = self.update_coordinates(coords[0],coords[1],20,20,60,20)
        coords = self.update_coordinates(coords[0],coords[1],0,-180,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-140)
        coords = self.update_coordinates(coords[0],coords[1],180,180,160,100)
        coords = self.update_coordinates(coords[0],coords[1],0,-140,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-100)
        coords = self.update_coordinates(coords[0],coords[1],-20,20,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        coords = self.update_coordinates(coords[0],coords[1],0,100,0,0)
        coords = self.update_coordinates(coords[0],coords[1],20,20,20,-20)
        coords = self.update_coordinates(coords[0],coords[1],20,-100,0,0)
        # Draw paths under left corner
        coords = self.update_coordinates(coords[0],coords[1],0,140,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,-80,20,20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,100,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,40)
        coords = self.update_coordinates(coords[0],coords[1],-80,-20,-20,-20)
        # Draw middle block (between left corner and stairs), starting from top to bottom
        coords = self.update_coordinates(coords[0],coords[1],40,40,160,80)
        coords = self.update_coordinates(coords[0],coords[1],0,20,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,0,140,80)
        coords = self.update_coordinates(coords[0],coords[1],20,20,-20,40)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],20,20,40,-60)
        coords = self.update_coordinates(coords[0],coords[1],20,0,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,40,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        #----- Draw the sideways T
        coords = self.update_coordinates(coords[0],coords[1],0,40,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,20,-20)
        #----- Draw the backwards C
        coords = self.update_coordinates(coords[0],coords[1],-40,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        #----- Draw the bottom line
        coords = self.update_coordinates(coords[0],coords[1],-60,60,-40,-40)
        # Draw the stairs, starting with the bottom of the stairs
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        # Draw top of stairs
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,-20,0)
        for i in range(3):
            coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
            coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        # Draw everything to the right of the stairs
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,80,20)
        coords = self.update_coordinates(coords[0],coords[1],280,200,60,60)
        coords = self.update_coordinates(coords[0],coords[1],-20,-180,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],40,40,-20,-60)
        coords = self.update_coordinates(coords[0],coords[1],-60,-20,20,20)
        coords = self.update_coordinates(coords[0],coords[1],20,-20,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-20,80,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-80,-80,0,-80)
        coords = self.update_coordinates(coords[0],coords[1],40,0,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,40,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,60)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,0,40)
        coords = self.update_coordinates(coords[0],coords[1],0,100,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],-20,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],40,40,20,0)
        coords = self.update_coordinates(coords[0],coords[1],0,60,00,0)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],20,60,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,-20,60)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,-20,20)
        coords = self.update_coordinates(coords[0],coords[1],60,60,-20,0)
        coords = self.update_coordinates(coords[0],coords[1],-60,120,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-100,-60,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],80,40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,40,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,40,40)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],-20,60,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,0,40)
        coords = self.update_coordinates(coords[0],coords[1],60,60,20,0)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],40,20,40,40)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],-20,0,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,40,20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        # Draw bottom right side
        coords = self.update_coordinates(coords[0],coords[1],60,20,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],0,-140,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,20,0)
        coords = self.update_coordinates(coords[0],coords[1],0,-60,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,-40,0,0)
        # Randomly choose which set of paths to close off
        close_paths = random.choice(["red","blue"])
        # Option 1 - "Blue and green paths"
        if close_paths == "blue":
            
            blue_line = self.update_coordinates(x_coordinate,top_coordinate,80,100,-180,-180)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],140,160,60,60)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],-20,10,40,40)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],30,30,100,80)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],40,40,20,0)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],0,0,-60,-80)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],-40,-40,-40,-60)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],60,90,-40,-40)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],130,150,20,20)
            blue_line = self.update_coordinates(blue_line[0],blue_line[1],40,40,100,80)
            # Randomly decide which "green" line to draw to close of that path, unless "stair" path does not dead ends, then draw both
            if did_stairs_end:
                if random.choice([True,False]):
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,340,370,-140,-140)
                else:
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,360,360,-160,-180)
            else:
                green_line = self.update_coordinates(x_coordinate,top_coordinate,340,370,-140,-140)
                green_line = self.update_coordinates(x_coordinate,top_coordinate,360,360,-160,-180)
                if top_coordinate == 10:
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,80,100,-100,-100)
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,240,260,-40,-40)
        # Option 2 - "red and green paths"
        if close_paths == "red":
            red_line = self.update_coordinates(x_coordinate,top_coordinate,260,260,20,0)
            red_line = self.update_coordinates(red_line[0],red_line[1],80,80,20,0)
            red_line = self.update_coordinates(red_line[0],red_line[1],20,0,-80,-80)
            red_line = self.update_coordinates(red_line[0],red_line[1],-100,-80,-20,-20)
            red_line = self.update_coordinates(red_line[0],red_line[1],0,0,-80,-60)
            red_line = self.update_coordinates(red_line[0],red_line[1],40,40,40,20)
            red_line = self.update_coordinates(red_line[0],red_line[1],40,40,20,-10)
            red_line = self.update_coordinates(red_line[0],red_line[1],-20,10,-30,-30)
            red_line = self.update_coordinates(red_line[0],red_line[1],90,90,20,40)
            red_line = self.update_coordinates(red_line[0],red_line[1],140,160,20,20)
            if did_stairs_end:
                if random.choice([True,False]):
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,180,200,-80,-80)
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,220,240,-40,-40)
                else:
                    green_line = self.update_coordinates(x_coordinate,top_coordinate,380,400,-120,-120)
            else:
                green_line = self.update_coordinates(x_coordinate,top_coordinate,180,200,-80,-80)
                green_line = self.update_coordinates(x_coordinate,top_coordinate,220,240,-40,-40)
                green_line = self.update_coordinates(x_coordinate,top_coordinate,380,400,-120,-120)
        return (top_coordinate-180)
                  
    def draw_third_row(self,top_coordinate):
        is_dead_end = self.draw_stair_paths(-390, top_coordinate)
        bottom = self.draw_many_random_choices(top_coordinate, is_dead_end)
        return bottom
    
    def draw_60_80_fourth_row(self):
        print("this is the 60 / 80 fourth row")
        
    def draw_100_fourth_row(self):
        print("this is the 100 fourth row")
        
    def draw_120_fourth_row(self):
        #draw left 3rd
        coords = self.update_coordinates(-390,-170,0,160,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],20,20,20,0)
        coords = self.update_coordinates(coords[0],coords[1],60,60,20,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,-20,-80)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,-200,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,60)
        coords = self.update_coordinates(coords[0],coords[1],0,60,0,0)
        coords = self.update_coordinates(coords[0],coords[1],20,120,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,-20,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,-180,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        for i in range(4):
            coords = self.update_coordinates(coords[0],coords[1],20,20,20,0)
            coords = self.update_coordinates(coords[0],coords[1],20,20,-20,0)
        # Randomly draw dead ends in left 3rd
        match random.randrange(0,3):
            case 0:
                green_line = self.update_coordinates(-390,-170,0,20,-80,-80)
                green_line = self.update_coordinates(green_line[0],green_line[1],140,140,60,40)
                green_line = self.update_coordinates(green_line[0],green_line[1],60,80,0,0)
            case 1:
                blue_line = self.update_coordinates(-390,-170,100,100,-40,-20)
                blue_line = self.update_coordinates(blue_line[0],blue_line[1],120,120,0,-20)
                blue_line = self.update_coordinates(blue_line[0],blue_line[1],0,-20,-60,-60)
            case 2:
                red_line = self.update_coordinates(-390,-170,80,80,-20,-41)
                red_line = self.update_coordinates(red_line[0],red_line[1],140,161,21,21)
        # Draw middle 3rd
        coords = self.update_coordinates(coords[0],coords[1],40,200,40,40)
        coords = self.update_coordinates(coords[0],coords[1],20,20,20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,-180,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,20,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,60,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],-40,-40,0,20)
        coords = self.update_coordinates(coords[0],coords[1],20,20,20,0)
        for i in range(2):
            coords = self.update_coordinates(coords[0],coords[1],20,20,-20,0)
        coords = self.update_coordinates(coords[0],coords[1],0,100,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],20,0,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,40,20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,-20,0)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-120,120,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,40)
        coords = self.update_coordinates(coords[0],coords[1],20,-20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,-20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,20,40)
        coords = self.update_coordinates(coords[0],coords[1],20,20,0,-80)
        coords = self.update_coordinates(coords[0],coords[1],-20,0,0,0)
        if random.choice([True, False]):
            temp_coord = self.update_coordinates(coords[0],coords[1],-180,-200,0,0)
        else:
            temp_coord = self.update_coordinates(coords[0],coords[1],-200,-200,20,40)
        # Draw right third
    
    def draw_forth_row(self,top_coordinate):
        ####################DELETE THIS LINE 60 and 80 = -130 top coord, 100 = -150 top coord, 120 = -170 top coord
        if top_coordinate >= -170:
            self.draw_120_fourth_row()
        if top_coordinate >= -150:
            self.draw_100_fourth_row()
        if top_coordinate >= -130:
            self.draw_60_80_fourth_row()