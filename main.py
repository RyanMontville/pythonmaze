from turtle import Turtle, mainloop, Screen
from generator import Generator
import random

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
screen.tracer(2,0)
generator = Generator()

generator.draw_grid()
generator.draw_border()
start_info = generator.draw_a(-390, 290, "top")
info = generator.draw_b(start_info[0],start_info[1],start_info[2])
info = generator.draw_d(info[0],info[1],start_info[2])
info = generator.draw_e(info[0],info[1],start_info[2])
info = generator.draw_f(info[0],info[1],start_info[2])
info = generator.draw_g(-390,50,start_info[2])


generator.update_coordinates(0,0,0,0,0,0)

screen.exitonclick()