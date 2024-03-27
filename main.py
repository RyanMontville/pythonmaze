from turtle import Turtle
from turtle import Screen
import random
from generator import Generator

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
# screen.tracer(0)
generator = Generator()
generator.go_to_top_left()
generator.print_cors()

# testing coordinate system
for i in range(2):
    generator.forward(780)
    generator.print_cors()
    generator.right(90)
    generator.forward(580)
    generator.print_cors()
    generator.right(90)

    






screen.exitonclick()