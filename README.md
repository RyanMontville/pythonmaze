# Python Maze Generator
Generate a maze in Python using [Turtle graphics](https://docs.python.org/3/library/turtle.html).

#### V 0.010 - 3/27/2024
First attempt at randomly generating a maze. The program starts at the top left corner, then heading down, randomly chooses if the next segment should be drawn in or not, then moves forwards 20px until it reaches the edge of the maze. It then moves to the right 20px and repeats until it has reached the right edge of the maze, which draws all of the vertical lines. It then does a similar process to draw all the horizontal lines.The generated maze most likely does not have a possible path from start to finish. This is more of a test to see what randomly generating the segments would do.

Here is an example of a randomly generated maze:
<p align="center" width="100%">
    <img width="50%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/first-attempt.png" alt="An example of a randomly generated maze" title="An example of a randomly generated maze">
</p>

#### V 0.020 - 3/30/2024
This attempt does not currently fill in the entire maze and is not truly random. I am testing having the program draw zig-zagging paths of random lengths. I want to test out having the program draw other shapes/patterns, then eventually have it choose a pattern at random to draw. Will update with an example screenshot after testing more patterns.

#### V 0.021 - 4/7/2024
This attempt is not truly random. I mapped out different patterns that can have variations to them with the program randomly blocking different pathways. There are 4 main sections that the program draws. While the maze will look similar every time it is run, the path from start to finish will change. There is currently a possibility that there is no possible path from start to finish, I need to figure out a way to ensure the program doesn't close off every possible path.