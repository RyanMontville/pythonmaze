from turtle import Turtle
from turtle import Screen
import random
from generator import Generator

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Maze Generator")
screen.tracer(1,0)
# screen.tracer(0)
generator = Generator()
generator.draw_border()


x_index = -370
print("loop starting now")
for i in range (38):
    generator.draw_line("down",x_index)
    x_index += 20

y_index = 270
print("loop starting now")
for i in range (28):
    generator.draw_line("right",y_index)
    y_index -= 20

    






screen.exitonclick()