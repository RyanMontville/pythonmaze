from turtle import Turtle, mainloop, Screen
from generator import Generator
import random

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
# screen.tracer(2,0)
generator = Generator()

generator.draw_zig_zags(-390,290)

screen.exitonclick()