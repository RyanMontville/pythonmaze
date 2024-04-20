# Python Maze Generator
Generate a maze in Python using [Turtle graphics](https://docs.python.org/3/library/turtle.html).

#### V 0.010 - 3/27/2024
First attempt at randomly generating a maze. The program starts at the top left corner, then heading down, randomly chooses if the next segment should be drawn in or not, then moves forwards 20px until it reaches the edge of the maze. It then moves to the right 20px and repeats until it has reached the right edge of the maze, which draws all of the vertical lines. It then does a similar process to draw all the horizontal lines.The generated maze most likely does not have a possible path from start to finish. This is more of a test to see what randomly generating the segments would do.

Here is an example of a randomly generated maze:
<p align="center" width="100%">
    <img width="50%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V010.png" alt="An example of a randomly generated maze" title="An example of a randomly generated maze">
</p>

#### V 0.020 - 3/30/2024
This attempt does not currently fill in the entire maze and is not truly random. I am testing having the program draw zig-zagging paths of random lengths. I want to test out having the program draw other shapes/patterns, then eventually have it choose a pattern at random to draw. Will update with an example screenshot after testing more patterns.

#### V 0.021 - 4/7/2024
This attempt is not truly random. I mapped out different patterns that can have variations to them with the program randomly blocking different pathways. There are 4 main sections that the program draws. While the maze will look similar every time it runs, the path from start to finish will change. There is currently a possibility that there is no possible path from start to finish, I need to figure out a way to ensure the program doesn't close off every possible path.

Here are some variations of V 0.021
<p align="center" width="100%">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/v021-A.png" alt="A variation of v 0.021" title="A variation of v 0.021">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V021-B.png" alt="A variation of v 0.021" title="A variation of v 0.021">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V021-C.png" alt="A variation of v 0.021" title="A variation of v 0.021">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V021-D.png" alt="A variation of v 0.021" title="A variation of v 0.021">
</p>

#### V 0.022 - 4/10/2024
I optimized the functions to reduce the file size. Now instead of printing the same command over and over again, the command now takes an array of cordinates and loops through them.

#### V 0.030 - 4/15/2024
Taking a differnet approach with this version. Instead of generating an entirely random maze, the program now asks the user to input a word or phrase and then generates a maze that spells out the word or phase as paths. I am reusing the functions from 0.020. I am currently working on drawing the letters and their paths.

#### V 0.031 - 4/15/2024
I have created the templates for every letter. Some letters are complete, some are still a work in progress. The program now prompts the user to enter a word or phrase that is 10 letters long or less. It then prints the word/phrase within the maze. Still need to create the rest of the maze around the letters. Might change the size of the maze to allow longer strings.
<p align="center" width="100%">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/a-l.png" alt="Current progress of letters A - L" title="Current progress of letters A - L">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/m-x.png" alt="Current progress of letters M - X" title="Current progress of letters M - X">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/y-z-spaces.png" alt="Current progress of letters Y, Z, and space variations" title="Current progress of letters Y, Z, and space variations">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/hello-world.png" alt="An example of the created maze" title="An example of the created maze">
</p>