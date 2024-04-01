from turtle import Turtle, mainloop, Screen
from generator import Generator
import random

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
# screen.tracer(2,0)
generator = Generator()

bottom_of_zig_zags = generator.draw_zig_zags(-390,290)
generator.draw_row(-390,bottom_of_zig_zags[0],bottom_of_zig_zags[1])


screen.exitonclick()