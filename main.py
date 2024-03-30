from turtle import Turtle, mainloop, Screen
from generator import Generator
import random

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
# screen.tracer(2,0)
generator = Generator()

x_coordinate = -370
total = 0
# random_vertical_length = random.choice([230,210,190,170])
random_lengths = [(230,"even"),(210,"odd"),(190,"both"),(170,"both")]
choice = random.choice(random_lengths)
random_vertical_length = choice[0]
random_vertical_length_up = random_vertical_length-20
range_options = []
if choice[1] == "even":
    range_options = [6,8,10,12,14]
elif choice[1] == "odd":
    range_options = [5,7,9,11,13,15]
elif choice[1] == "both":
    range_options = [5,6,7,8,9,10,11,12,13,14,15]
for i in range(random.choice(range_options)):
    x_offset = x_coordinate + (i*20)
    if i%2 == 0:
        generator.draw_line_from_tuple((x_offset,290,x_offset,random_vertical_length))
    else:
        generator.draw_line_from_tuple((x_offset,random_vertical_length_up,x_offset,270))
    total += 1
print("total: " + str(total) + ", vertical: " + str(random_vertical_length))
bottom_line = -390 + (total * 20)
generator.draw_line_from_tuple((-390,random_vertical_length_up,bottom_line,random_vertical_length_up))
print(total)
x_start_point = bottom_line
x_offset_point = bottom_line + 20
horizontal_offset = 0
if total % 2 == 0:
    horizontal_offset = 270
    horizontal_count = 0
    while horizontal_offset > (random_vertical_length_up-20):
        if horizontal_count % 2 == 0:
            generator.draw_line_from_tuple((x_start_point,horizontal_offset,370,horizontal_offset))
            horizontal_offset -= 20
            horizontal_count += 1
        else:
            generator.draw_line_from_tuple((390,horizontal_offset,x_offset_point,horizontal_offset))
            horizontal_offset -= 20
            horizontal_count += 1
else:
    horizontal_offset = random_vertical_length_up
    horizontal_count = 0
    generator.draw_line_from_tuple((x_offset,horizontal_offset,370,horizontal_offset))
    horizontal_offset += 20
    while horizontal_offset < 290:
        if horizontal_count % 2 == 0:
            generator.draw_line_from_tuple((x_start_point,horizontal_offset,350,horizontal_offset))
            horizontal_offset += 20
            horizontal_count += 1
            generator.draw_line_from_tuple((370,270,370,random_vertical_length_up))
        else:
            generator.draw_line_from_tuple((370,horizontal_offset,x_offset_point,horizontal_offset))
            horizontal_offset += 20
            horizontal_count += 1
        
    
    




mainloop()