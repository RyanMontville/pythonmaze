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
start_info = generator.draw_b(-390, 290, "top")
info = generator.draw_c(start_info[0],start_info[1],start_info[2])
info = generator.draw_d(info[0],info[1],start_info[2])
info = generator.draw_g(info[0],info[1],start_info[2])
info = generator.draw_o(info[0],info[1],start_info[2])
info = generator.draw_p(-390,50,start_info[2])
info = generator.draw_q(info[0],info[1],start_info[2])
info = generator.draw_r(info[0],info[1],start_info[2])
info = generator.draw_k(info[0],info[1],start_info[2])
info = generator.draw_l(info[0],info[1],start_info[2])

generator.update_coordinates(0,0,0,0,0,0)

screen.exitonclick()