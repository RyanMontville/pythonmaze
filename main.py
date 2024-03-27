from turtle import Turtle
from turtle import Screen
import random
from generator import Generator

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
screen.tracer(25,0)
generator = Generator()
generator.hideturtle()
generator.draw_border()

generator.draw_all_vertical()
generator.draw_all_horizontal()


    






screen.exitonclick()