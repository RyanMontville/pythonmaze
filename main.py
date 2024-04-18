from turtle import Turtle, mainloop, Screen
from generator import Generator
import random

def prompt_for_letters():
    word = input("Type a word or phrase 12 letter long or less: ")
    while True:
        if len(word) > 12:
            print(f"Error! Word or Phase can't be longer than 12 letters. You entered {len(word)} letters.")
            word = input("Type a word or phrase 12 letter long or less: ")
        else:
            return word.lower()

def format_string(word):
    words = word.split()
    line_one = ""
    if len(words) == 1:
        line_one = word[:6]
        line_two = word[6:]
    elif len(words[0]) == 6:
        line_one = words[0]
        line_two = word[6:]
    elif len(words[0]) + len(words[1]) < 6:
        line_one = words[0] + " " + words[1]
        line_two = word[len(line_one):]
    else:
        line_one = words[0]
        line_two = word[len(line_one):]
    line_one_final = line_one.strip()
    line_two_final = line_two.strip()
    while len(line_one_final) < 6:
        line_one_final += "-"
    while len(line_two_final) < 6:
        line_two_final += "-"
    return (line_one_final,line_two_final)

def draw_letter_return_info(info, letter):
    match letter:
        case "a":
            return generator.draw_a(info[0],info[1],info[2])
        case "b":
            return generator.draw_b(info[0],info[1],info[2])
        case "c":
            return generator.draw_c(info[0],info[1],info[2])
        case "d":
            return generator.draw_d(info[0],info[1],info[2])
        case "e":
            return generator.draw_e(info[0],info[1],info[2])
        case "f":
            return generator.draw_f(info[0],info[1],info[2])
        case "g":
            return generator.draw_g(info[0],info[1],info[2])
        case "h":
            return generator.draw_h(info[0],info[1],info[2])
        case "i":
            return generator.draw_i(info[0],info[1],info[2])
        case "j":
            return generator.draw_j(info[0],info[1],info[2])
        case "k":
            return generator.draw_k(info[0],info[1],info[2])
        case "l":
            return generator.draw_l(info[0],info[1],info[2])
        case "m":
            return generator.draw_m(info[0],info[1],info[2])
        case "n":
            return generator.draw_n(info[0],info[1],info[2])
        case "o":
            return generator.draw_o(info[0],info[1],info[2])
        case "p":
            return generator.draw_p(info[0],info[1],info[2])
        case "q":
            return generator.draw_q(info[0],info[1],info[2])
        case "r":
            return generator.draw_r(info[0],info[1],info[2])
        case "s":
            return generator.draw_s(info[0],info[1],info[2])
        case "t":
            return generator.draw_t(info[0],info[1],info[2])
        case "u":
            return generator.draw_u(info[0],info[1],info[2])
        case "v":
            return generator.draw_v(info[0],info[1],info[2])
        case "w":
            return generator.draw_w(info[0],info[1],info[2])
        case "x":
            return generator.draw_x(info[0],info[1],info[2])
        case "y":
            return generator.draw_y(info[0],info[1],info[2])
        case "z":
            return generator.draw_z(info[0],info[1],info[2])
        case _:
            return generator.draw_space(info[0],info[1],info[2])

word_to_create = prompt_for_letters()
lines = format_string(word_to_create)
screen = Screen()
screen.setup(width=920,height=600)
screen.title("Maze Generator")
screen.tracer(2,0)
generator = Generator()

#generator.draw_grid()
generator.draw_border()
info = (-450,290,"Top")
for i in lines[0]:
    info = draw_letter_return_info(info,i)
generator.draw_row_one_end(True)
info = (-430,50,"top")
for i in lines[1]:
    info = draw_letter_return_info(info,i)
generator.two_row_finish()


generator.update_coordinates(0,0,0,0,0,0)

screen.exitonclick()