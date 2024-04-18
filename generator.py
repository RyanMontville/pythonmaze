from turtle import Turtle
import random

class Generator(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_border()
        self.hideturtle()
        self.speed("fastest")
        self.normal = 1
        self.bold = 3
        
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
        border_start = (-450,290,0,880,0,0)
        border_array = [(0,0,0,-560),(0,-880,-20,-20),(0,0,0,560)]
        self.update_coordinates_from_array(border_start,border_array)
    
    def reset_coordinates(self,x_cord,y_cord):
        self.pu()
        self.goto(x_cord,y_cord)

    def draw_circle(self,x_offset,y_offset,radius,angle,heading):
        self.reset_coordinates(self.xcor()+x_offset,self.ycor()+y_offset)
        self.pd()
        self.setheading(heading)
        self.circle(radius, angle)
        
    def draw_grid(self):
        self.pencolor("LightGrey")
        coords = self.update_coordinates(-450,270,0,880,0,0)
        while coords[1] > -270:
            coords = self.update_coordinates(-450,coords[1],0,880,-20,-20)
        coords = self.update_coordinates(-430,290,0,0,0,-580)
        while coords[0] < 430:
            coords = self.update_coordinates(coords[0],290,20,20,0,-580)
        self.pencolor("black")

    def draw_right_side(self,start_x,start_y):
        self.update_coordinates(start_x,start_y,0,140,-240,-240)
        if random.choice([True, False]):
            self.update_coordinates(start_x + 140, start_y,0,0,0,-220)
            return (start_x + 140, start_y,"bottom")
        else:
            self.update_coordinates(start_x + 140, start_y,0,0,-20,-240)
            return (start_x + 140, start_y,"top")

    def draw_a(self,start_x, start_y,top_or_bottom):
        #Draw the A
        self.pensize(self.bold)
        start_coords = (start_x,start_y,40,70,-180,-40)
        coords_array = [(20,50,0,-140),(-20,-30,0,60),(0,-20,0,0),(0,-10,0,-60),(10,15,80,110),(0,10,0,0),
                        (0,5,0,-30),(0,-20,0,0)]
        self.update_coordinates_from_array(start_coords,coords_array)
        self.pensize(self.normal)
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
            self.pensize(self.bold)
            if random.choice([True, False]):
                self.update_coordinates(close_coords[0],close_coords[1],-10,10,-20,-20)
            else:
                self.update_coordinates(close_coords[0],close_coords[1],-20,-40,-160,-160)
            self.pensize(self.normal)
        else:
            self.pensize(self.bold)
            close_coords = self.update_coordinates(start_x,start_y,70,90,-40,-40)
            self.pensize(self.normal)
            close_coords = self.update_coordinates(close_coords[0],close_coords[1],-10,-10,-180,-200)
        #close off top or bottom exit
        return self.draw_right_side(start_x,start_y)
        
    def draw_b(self,start_x, start_y,top_or_bottom):
        #Draw the B
        self.pensize(self.bold)
        start_coords = (start_x,start_y,20,20,-180,-80)
        coords_array = [(0,20,20,20),(-20,0,-140,-140),(0,0,125,85),(0,0,-30,-70),(0,0,-15,-15)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        for i in range(2):
            self.draw_circle(0,0,35,180, 0)
        self.draw_circle(0,-125,20,180, 0)
        self.draw_circle(0,30,20,180, 0)
        self.pensize(self.normal)
        #Draw the paths around the B, starting from the top
        start_coords = (start_x,start_y,20,20,-60,-20)
        coords_array = [(0,60,0,0),(40,40,20,-40),(-20,-20,-120,40),(0,-60,-20,-20),(40,40,-20,-40),
                        (0,-10,0,0),(5,18,-20,-20),(11,-9,-20,-20),(-15,10,-20,-20),(10,-5,-20,-20),
                        (16,36,-20,-20),(20,0,100,100),(0,-20,-20,-20),(0,40,-20,-20),(-40,-20,-20,-20),
                        (20,0,-20,-20),(0,0,-20,-60),(-20,-20,0,20),(0,-20,0,0),(0,-20,-20,-20),
                        (0,0,0,26),(-20,-20,-46,-26),(-20,-20,20,0),(-20,120,-20,-20)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        if top_or_bottom == "top":
            start_coords = (start_x,start_y,20,20,0,-20)
            coords_array = [(-20,0,-160,-160),(80,80,-40,-60)]
            self.update_coordinates_from_array(start_coords,coords_array)
        else:
            start_coords = (start_x,start_y,0,20,-80,-80)
            coords_array = [(60,60,-160,-140),(20,41,0,0)]
            self.update_coordinates_from_array(start_coords,coords_array)

        #draw the right side line, closing off either the top or bottom
        return self.draw_right_side(start_x,start_y)
    
    def draw_c(self,start_x, start_y,top_or_bottom):
        #Draw the C
        self.pensize(self.bold)
        self.reset_coordinates(start_x,start_y)
        self.draw_circle(90,-60,40,180,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,-60)
        self.draw_circle(0,0,40,180,270)
        self.draw_circle(-60,0,20,180,270)
        self.update_coordinates(self.xcor(),self.ycor(),-40,-40,0,60)
        self.draw_circle(40,0,20,180,90)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)

    def draw_d(self,start_x, start_y,top_or_bottom):
        #Draw the D
        self.pensize(self.bold)
        self.update_coordinates(start_x,start_y,40,40,-40,-180)
        self.draw_circle(20,0,60,90,0)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,20)
        self.draw_circle(0,0,60,90,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,-20,-120)
        self.draw_circle(0,0,40,90,0)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,20)
        self.draw_circle(0,0,40,90,90)
        self.pensize(self.normal)
        #Draw the paths
        start_coords = (start_x,start_y,20,40,-20,-20)
        coord_array = [(0,0,0,-20),(-40,-20,0,0),(20,0,-20,-20),(-20,0,-20,-20),(20,0,-20,-20),
                       (-20,0,-20,-20),(20,0,-20,-20),(-20,0,-20,-20),(20,0,-20,-20),(0,0,0,-40),
                       (-20,120,-20,-20),(-100,-100,0,40),(20,20,20,-20),(20,20,-20,20),(0,40,0,0),
                       (-20,20,-20,-20),(-65,-20,40,40),(0,20,20,20),(0,-20,100,100),(-45,0,20,20),
                       (20,-40,20,20),(-20,-20,0,-20)]
        coords = self.update_coordinates_from_array(start_coords,coord_array)
        if top_or_bottom == "top":
            if random.choice([True, False]):
                # Draw the lines to close off the paths if enter from the top
                closed_coord = self.update_coordinates(coords[0],coords[1],0,0,20,40)
                closed_coord = self.update_coordinates(closed_coord[0],closed_coord[1],-40,-60,-20,-20)
            else:
                closed_coord = self.update_coordinates(coords[0],coords[1],-20,-20,40,20)
                closed_coord = self.update_coordinates(closed_coord[0],closed_coord[1],20,40,-200,-200)
        else:
            # Draw the lines to colse off the paths if enter from the bottom
            if random.choice([True, False]):
                closed_coord = self.update_coordinates(coords[0],coords[1],0,0,40,20)
                closed_coord = self.update_coordinates(closed_coord[0],closed_coord[1],-20,-20,-160,-180)
            else:
                closed_coord = self.update_coordinates(coords[0],coords[1],-60,-40,20,20)
                closed_coord = self.update_coordinates(closed_coord[0],closed_coord[1],40,40,-220,-200)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
        
    def draw_e(self,start_x, start_y,top_or_bottom):
        # Draw the E
        self.pensize(self.bold)
        start_coords = (start_x,start_y,20,100,-20,-20)
        coord_Array =[(0,-60,-20,-20),(0,0,0,-40),(0,40,0,0),(0,-40,-20,-20),
                      (0,0,0,-40),(0,60,0,0),(0,-80,-20,-20),(0,0,0,120)]
        coords = self.update_coordinates_from_array(start_coords,coord_Array)
        self.pensize(self.normal)
        # Draw the paths, starting from the bottom
        start_coords = (coords[0],coords[1],0,0,-120,-200)
        coord_Array = [(-20,120,0,0),(-60,-20,20,20),(0,-60,20,20),(0,0,0,-20),
                       (-20,-20,0,40),(0,100,0,0),(-20,-40,20,20),(0,20,20,20),
                       (-60,0,20,20),(0,0,0,40),(0,-40,0,0),(-20,40,20,20),
                       (0,0,0,60),(-120,-100,-20,-20)]
        coords = self.update_coordinates_from_array(start_coords,coord_Array)
        # Close off 2 of the E exit paths
        match random.choice([1,2,3]):
            case 1:
                exit = self.update_coordinates(coords[0],coords[1],100,100,-100,-120)
                exit = self.update_coordinates(exit[0],exit[1],0,0,0,-20)
            case 2:
                exit = self.update_coordinates(coords[0],coords[1],100,100,-40,-60)
                exit = self.update_coordinates(exit[0],exit[1],0,0,-60,-80)
            case 3:
                exit = self.update_coordinates(coords[0],coords[1],100,100,-40,-60)
                exit = self.update_coordinates(exit[0],exit[1],0,0,-40,-60)
        # Draw one of 4 bottom path configurations
        match random.choice([1,2,3,4]):
            case 1:
                block = self.update_coordinates(start_x,start_y,60,60,-220,-240)
                block = self.update_coordinates(block[0],block[1],20,20,0,20)
            case 2:
                block = self.update_coordinates(start_x,start_y,60,60,-220,-240)
                block = self.update_coordinates(block[0],block[1],60,80,20,20)
            case 3:
                block = self.update_coordinates(start_x,start_y,60,80,-220,-220)
                block = self.update_coordinates(block[0],block[1],40,40,0,-20)
            case 4:
                block = self.update_coordinates(start_x,start_y,120,120,-180,-200)
                block = self.update_coordinates(block[0],block[1],-40,-40,-20,-40)
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_f(self,start_x, start_y,top_or_bottom):
        # Draw the F
        self.pensize(self.bold)
        start_coords = (start_x,start_y,20,100,-20,-20)
        coord_Array =[(0,-60,-20,-20),(0,0,0,-40),(0,40,0,0),(0,-40,-20,-20),
                      (0,0,0,-60),(-20,-20,0,120)]
        coords = self.update_coordinates_from_array(start_coords,coord_Array)
        self.pensize(self.normal)
        # Draw the shared paths
        coord_Array = [(0,20,0,0),(0,0,0,-40),(0,-60,0,0),(80,20,-20,-20),
                       (0,40,-20,-20),(0,0,0,-120),(20,-120,-20,-20),(20,100,20,20),
                       (0,0,0,100),(0,-40,0,0),(0,0,0,-60),(20,20,40,-20),(0,-40,0,0),
                       (0,0,0,40),(-40,-20,40,40),(-20,0,-60,-60),(20,0,-20,-20),
                       (-20,0,-20,-20),(60,60,220,200)]
        coords = self.update_coordinates_from_array(start_coords,coord_Array)
        if top_or_bottom == "top":
            coords = self.update_coordinates(coords[0],coords[1],40,60,-200,-200)
        else :
            coords = self.update_coordinates(coords[0],coords[1],40,40,-200,-220)
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_g(self,start_x, start_y,top_or_bottom):
        # Draw the G
        self.pensize(self.bold)
        self.reset_coordinates(start_x,start_y)
        self.draw_circle(120,-140,40,180,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,-20,-60)
        self.draw_circle(0,0,40,180,270)
        self.draw_circle(-60,0,20,180,270)
        self.update_coordinates(self.xcor(),self.ycor(),-40,-40,0,60)
        self.draw_circle(40,0,20,180,90)
        start_coords = (self.xcor(),self.ycor(),40,30,-60,-60)
        coords_array = [(0,0,0,20),(0,50,0,0),(0,0,0,-40),(-20,-20,0,20)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        self.pensize(self.normal)
        # Draw the paths
        start_coords = (start_x,start_y,20,20,-220,-20)
        coords_array = [(0,40,-20,-20),(0,40,-20,-20),(0,0,-20,40),(-20,-20,20,-20),
                        (0,0,-60,-40),(-20,-20,0,60),(-20,-20,20,0),(0,0,-40,-120),
                        (35,35,-60,0),(0,45,-20,-20),(0,0,0,160)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        # Draw a line to close off one of the paths
        if random.choice([True, False]):
            self.update_coordinates(coords[0],coords[1],-100,-100,-220,-240)
        else:
            self.update_coordinates(coords[0],coords[1],-20,-40,-80,-80)
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_h(self,start_x, start_y,top_or_bottom):
        # Draw the H
        self.pensize(self.bold)
        start_coords = (start_x,start_y,40,40,-40,-160)
        coords_array = [(0,20,-20,-20),(0,0,0,60),(0,40,0,0),(0,0,0,-60),
                        (0,20,0,0),(0,0,20,120),(0,-20,20,20),(0,0,0,-60),
                        (0,-40,0,0),(0,0,0,40),(0,-20,20,20)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        self.pensize(self.normal)
        # Draw the paths
        start_coords = (coords[0],coords[1],-20,60,20,20)
        coords_array = [(-20,-20,0,-60),(0,-20,40,40),(-40,-40,20,-100),(-20,0,0,0),
                        (20,0,-20,-20),(0,0,0,-60),(80,0,0,0),(0,80,20,20),(-20,-20,60,0),
                        (40,40,-40,20),(20,0,80,80),(0,0,60,100)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_i(self,start_x, start_y,top_or_bottom):
        # Draw the I
        self.pensize(self.bold)
        start_coords = (start_x,start_y,30,60,-40,-40)
        coords_array = [(0,0,0,-100),(0,-30,0,0),(0,80,-20,-20),(0,-30,20,20),(0,0,0,100),
                        (0,30,0,0),(0,-80,20,20)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        # Close one of the entrances
        if random.choice([True, False]):
            self.update_coordinates(start_x,start_y,30,30,-20,-40)
        else:
            self.update_coordinates(start_x,start_y,30,30,-140,-160)
        # Close one of the exits
        if random.choice([True, False]):
            self.update_coordinates(start_x,start_y,110,110,-20,-40)
        else:
            self.update_coordinates(start_x,start_y,110,110,-140,-160)
        self.pensize(self.normal)
        # Draw the paths
        start_coords = (coords[0],coords[1],-13,-30,0,0)
        coords_array = [(15,30,-20,-20),(-30,10,-20,-20),(0,0,0,-60),(-10,-20,-20,-20),
                        (0,0,60,0),(-3,-20,-20,-20),(120,10,-20,-20),(-10,10,-20,-20),
                        (-3,10,-20,-20),(0,0,-20,40),(90,40,-40,-40),(0,0,-20,0),
                        (-20,-20,0,20),(0,90,0,0),(-20,-20,20,40),(-10,0,0,0),
                        (-40,0,40,40),(0,0,0,40),(-20,-20,-20,20),(0,40,0,0),(-30,-30,40,60)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_j(self,start_x, start_y,top_or_bottom):
        # Draw the J
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,20,-60,-80) # Top left
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-90)
        self.draw_circle(-20,0,10,180,270)
        coords = self.update_coordinates(coords[0],coords[1],-20,-40,0,0) # bottom of J
        self.draw_circle(0,0,30,180,270)
        coords = self.update_coordinates(coords[0],coords[1],60,60,0,90)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20) # top right
        coords = self.update_coordinates(coords[0],coords[1],0,-80,0,0)
        self.pensize(self.normal)
        # Draw the paths
        
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_k(self,start_x, start_y,top_or_bottom):
        # Draw the K
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,40,40,-40,-180)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom left
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,60)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom right
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,70)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,70)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # Top right
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,60)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # Top left
        self.pensize(self.normal)
        # Draw the paths
        
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_l(self,start_x, start_y,top_or_bottom):
        # Draw the L
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,40,40,-40,-160) # bottom left is open
        coords = self.update_coordinates(coords[0],coords[1],0,80,-20,-20)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20) # bottom right
        coords = self.update_coordinates(coords[0],coords[1],0,-60,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,120)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # top of L
        self.pensize(self.normal)
        # Draw the paths
        
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_m(self,start_x, start_y,top_or_bottom):
        # Draw the M
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,20,-40,-180)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom left
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,40)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom right
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,140)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # top right
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,40)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # top left
        self.pensize(self.normal)
        # Draw the paths
        
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_n(self,start_x, start_y,top_or_bottom):
        # Draw the N
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,20,-40,-180)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom left
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,100)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom right
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,140)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # top right
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,100)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,0) # top left

        self.pensize(self.normal)
        # Draw the paths
        
        # Draw the right side
        return self.draw_right_side(start_x,start_y)
    
    def draw_o(self,start_x, start_y,top_or_bottom):
        #Draw the O
        self.pensize(self.bold)
        self.reset_coordinates(start_x,start_y)
        self.draw_circle(100,-60,40,180,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,-60)
        self.draw_circle(0,0,40,180,270)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,60)
        self.draw_circle(-20,0,20,180,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,-60)
        self.draw_circle(0,0,20,180,270)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,60)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_p(self,start_x, start_y,top_or_bottom):
        #Draw the P
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,20,-40,-180)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom of P
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,60) 
        self.draw_circle(0,0,40,180,0) # Top of P is open
        coords = self.update_coordinates(self.xcor(),self.ycor(),-5,-5,-20,-60)
        self.draw_circle(0,0,20,180,0)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_q(self,start_x, start_y,top_or_bottom):
        #Draw the Q
        self.pensize(self.bold)
        self.reset_coordinates(start_x-10,start_y)
        self.draw_circle(110,-60,39,180,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,-20,-60) # left side top of Q open
        self.draw_circle(0,0,35,160,270)
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,10,0,-20)
        #coords = self.update_coordinates(coords[0],coords[1],0,20,0,20) # bottom of Q
        coords = self.update_coordinates(coords[0],coords[1],10,0,20,40) 
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,30) # right side top of Q open
        self.draw_circle(-20,20,20,180,90)
        self.update_coordinates(self.xcor(),self.ycor(),0,0,0,-60)
        self.draw_circle(0,0,15,170,270)
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,-10,0,15)
        coords = self.update_coordinates(coords[0],coords[1],0,15,0,10)
        coords = self.update_coordinates(coords[0],coords[1],0,5,0,-10)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,47)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_r(self,start_x, start_y,top_or_bottom):
        #Draw the R
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,20,-20,-160)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom left
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,60)
        coords = self.update_coordinates(coords[0],coords[1],0,40,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom right
        coords = self.update_coordinates(coords[0],coords[1],0,-40,0,60)
        self.draw_circle(0,0,40,180,0) 
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,-20,0,0) # Top of R is open ( could do -40 to close it)
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,0,-20,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0)
        self.draw_circle(0,0,20,180,0)
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,-20,0,0)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_s(self,start_x, start_y,top_or_bottom):
        # Draw the S
        self.pensize(self.bold)
        self.reset_coordinates(start_x + 120, start_y - 80)
        self.draw_circle(0,0,40,270,90)
        self.draw_circle(-20,-20,20,270,270)
        self.reset_coordinates(self.xcor()-40,self.ycor()-20)
        self.draw_circle(0,0,40,270,270)
        self.draw_circle(20,20,20,270,90)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_t(self,start_x, start_y,top_or_bottom):
        # Draw the T
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,20,-60,-80) # Top left
        coords = self.update_coordinates(coords[0],coords[1],0,30,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-120)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,0) # bottom of T
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,120)
        coords = self.update_coordinates(coords[0],coords[1],0,30,0,0)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,20) # top right
        coords = self.update_coordinates(coords[0],coords[1],0,-80,0,0)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_u(self,start_x, start_y,top_or_bottom):
        # Draw the U
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,40,40,-80,-180)
        self.draw_circle(0,0,40,180,270)
        coords = self.update_coordinates(self.xcor(),self.ycor(),0,0,0,100)
        coords = self.update_coordinates(coords[0],coords[1],-20,-20,0,-100)
        self.draw_circle(-40,0,20,180,270)
        coords = self.update_coordinates(self.xcor(),self.ycor(),-40,-40,0,100)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_v(self,start_x, start_y,top_or_bottom):
        # Draw the V
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,20,50,-40,-180)
        coords = self.update_coordinates(coords[0],coords[1],20,50,0,140) # bottom is open
        coords = self.update_coordinates(coords[0],coords[1],-20,-40,0,-90)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,90)
        
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_w(self,start_x, start_y,top_or_bottom):
        # Draw the W
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,60,70,-20,-160)
        coords = self.update_coordinates(coords[0],coords[1],20,30,0,40)
        coords = self.update_coordinates(coords[0],coords[1],0,10,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],20,30,0,140)
        coords = self.update_coordinates(coords[0],coords[1],-20,-25,0,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,-15,0,40)
        coords = self.update_coordinates(coords[0],coords[1],0,-15,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-5,0,100)
        
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_x(self,start_x, start_y,top_or_bottom):
        # Draw the X
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,40,70,-40,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,-30,0,-80)
        coords = self.update_coordinates(coords[0],coords[1],20,40,0,60)
        coords = self.update_coordinates(coords[0],coords[1],0,20,0,-60)
        coords = self.update_coordinates(coords[0],coords[1],20,-10,0,80)
        coords = self.update_coordinates(coords[0],coords[1],0,30,0,60)
        coords = self.update_coordinates(coords[0],coords[1],-20,-40,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,40)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_y(self,start_x, start_y,top_or_bottom):
        # Draw the Y
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,40,70,-40,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,0,0,-80)
        coords = self.update_coordinates(coords[0],coords[1],20,20,0,80)
        coords = self.update_coordinates(coords[0],coords[1],0,30,0,60)
        coords = self.update_coordinates(coords[0],coords[1],-20,-40,0,-40)
        coords = self.update_coordinates(coords[0],coords[1],0,-20,0,40)
        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_z(self,start_x, start_y,top_or_bottom):
        # Draw the Z
        self.pensize(self.bold)
        coords = self.update_coordinates(start_x,start_y,40,100,-60,-60)
        coords = self.update_coordinates(coords[0],coords[1],0,-60,0,-100)
        coords = self.update_coordinates(coords[0],coords[1],0,80,-20,-20) 
        coords = self.update_coordinates(coords[0],coords[1],0,-60,20,20)
        coords = self.update_coordinates(coords[0],coords[1],0,60,0,100)
        coords = self.update_coordinates(coords[0],coords[1],0,-80,20,20)

        self.pensize(self.normal)
        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_space(self,start_x, start_y,top_or_bottom):
        

        # Draw the right side, closing off the top or bottom, then return the info
        return self.draw_right_side(start_x,start_y)
    
    def draw_row_one_end(self, draw_second_row_ends):
        start_coords = (430,290,-20,-20,-20,-40)
        coords_array = [(-20,0,0,0),(20,0,-20,-20),(-20,0,-20,-20),(0,0,0,-20),(20,0,-20,-20),
                        (-20,0,-20,-20),(20,0,-20,-20),(0,0,0,-20),(-20,0,-20,-20),(20,0,-20,-20),
                        (-20,0,-20,-20)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        if draw_second_row_ends:
            coords = self.update_coordinates(coords[0],coords[1],20,-1,-240,-240)
            coords = self.update_coordinates(-430,coords[1],0,0,0,220)

    def two_row_finish(self):
        start_coords = (-450,-290,0,120,20,20)
        coords_array = [(20,20,-20,20),(0,-120,0,0),(0,200,20,20),(-60,-60,0,-40),(20,20,-20,20),
                        (20,20,20,-20),(20,20,-20,20),(-200,60,40,40),(-40,-40,0,-60),(0,20,0,0),
                        (0,0,0,20),(0,20,0,0),(0,0,0,20),(-20,20,0,0),(0,0,0,20),(0,20,0,0),
                        (20,20,0,-40),(0,-20,20,20),(0,0,0,-20),(0,-20,0,0),(0,0,0,-20),
                        (0,-20,0,0),(0,0,0,-20),(40,60,20,20),(0,0,-20,0),(20,20,80,0),
                        (0,80,0,0),(0,0,0,40),(0,-40,0,0),(20,-20,-20,-20),(0,0,0,40),
                        (0,80,0,0),(0,0,0,-80),(20,20,20,80),(20,20,-20,-80),(20,20,20,80),
                        (20,20,-20,-80),(20,20,20,80),(20,20,-20,-80),(20,20,20,80),
                        (-120,0,0,0),(20,20,20,-20),(0,0,-20,-40),(20,20,-20,0),(20,20,20,0),
                        (20,20,-20,0),(20,20,20,0),(20,20,-20,0),(20,20,20,0),(20,20,-20,0),
                        (20,20,20,0),(20,20,-20,0),(20,20,20,0),(20,20,-20,0),(20,20,0,60),
                        (0,-220,0,0),(-20,200,-20,-20),(20,-220,-20,-20)]
        coords = self.update_coordinates_from_array(start_coords,coords_array)
        match random.choice([1, 2, 3]):
            case 1:
                coords = self.update_coordinates(-230,-290,0,0,40,60)
                self.update_coordinates(coords[0],coords[1],100,120,20,20)
            case 2:
                self.update_coordinates(-130,-290,0,0,100,80)
                self.update_coordinates(-230,-290,0,0,40,60)
            case 3:
                self.update_coordinates(-130,-290,0,0,100,80)
                self.update_coordinates(-230,-290,0,20,60,60)
        if random.choice([True, False]):
            self.update_coordinates(150,-290,0,0,100,78)
        else:
            self.update_coordinates(150,-290,0,0,0,20)
        if random.choice([True, False]):
            self.update_coordinates(190,-290,0,0,100,80)
        else:
            self.update_coordinates(330,-290,0,0,0,21)
        
