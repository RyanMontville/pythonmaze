# Python Maze Generator
I wanted to try to use [Turtle graphics](https://docs.python.org/3/library/turtle.html) to randomly generate mazes using python. I still consider this project a work in progress because I have not yet achieved the level of randomness that I imagined when I started this project.

### Version 1
For my first attempt, I created a grid and then had the program randomly draw lines on the grid. It <i>Kinda</i> looks like a maze at first glance, but the paths are not continuous and most of the time it is impossible to go from the start of the maze to the finish. You can see an example of the random lines below. It was a good experiment at what randomly drawing lines can do, but I knew I could do better.

Generate a maze in Python using .
<p align="center" width="100%">
    <img width="50%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V010.png" alt="An example of a randomly generated maze" title="An example of a randomly generated maze">
</p>
<a href="https://ryanmontville.github.io/pythonmaze/version-one.html">Run the version 1 generator</a>

### Version 2
Next, I decided to draw a few different patterns. Some of the patterns could vary in width and height, while other patterns randomly decieded which paths were dead-ends and which paths would lead you into the next section of the maze. It still wasn't as random as I was hoping for, but it was good progress. With the amount of random decisions the program made, even though the maze will look similar overall each time it is generated, the path from start to finish will always be different. I knew I could still do better.

Here are several examples below with the path from start to finish highlighted:
<p align="center" width="100%">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/v021-A.png" alt="A variation of v 0.021" title="A variation of v 0.021">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V021-B.png" alt="A variation of v 0.021" title="A variation of v 0.021">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V021-C.png" alt="A variation of v 0.021" title="A variation of v 0.021">
    <img width="23%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/V021-D.png" alt="A variation of v 0.021" title="A variation of v 0.021">
</p>
<a href="https://ryanmontville.github.io/pythonmaze/version-two.html">Run the version 2 generator</a>

### Version 3
While looking at mazes online, I found a maze generator that could generate mazes in several different patterns, including mazes that aren't just rectangular. One of the mazes was in an "X" pattern, which gave me the idea to try to make a generator where you could type a word or phrase and have a maze generated with the letters making up the maze. I started planning by drawing the letters, then taking screenshots of the letters into Photoshop to draw the paths around and through the letters. Each letter is a function that takes the coordinates of the top-left corner of the letter segment and whether the path into the segment from the last segment is on the top or bottom. Every letter randomly chooses whether  you exit the segment through the top or bottom and passes it on to the next segment. Some letters generate different paths depending on if you enter from the top or the bottom. Some letters randomly decide which paths will be dead-ends while other letters always have the same paths through the segment. While this version of the maze generator is different from my plan when I started this project, I am happy with how it turned out.

Here are all of the letters with the grid lines showing along with the different choices for the spaces between words:
<p align="center" width="100%">
    <img width="31%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/A-I.png" alt="Examples of letters A - I" title="Examples of letters A - I">
    <img width="31%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/J-R.png" alt="Examples of letters J - R" title="Examples of letters J - R">
    <img width="31%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/S-Z.png" alt="Examples of letters S - Z" title="Examples of letters S - Z">
</p>

Here are a few examples of the maze generated from a phrase:
<p align="center" width="100%">
<img width="31%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/hello-world.png" alt="An example of the created maze" title="An example of the created maze">
<img width="31%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/a-cool-monkey.png" alt="An example of the created maze" title="An example of the created maze">
<img width="31%" src="https://github.com/RyanMontville/pythonmaze/blob/main/images/montville.png" alt="An example of the created maze" title="An example of the created maze">
</p>
<a href="https://ryanmontville.github.io/pythonmaze/version-three.html">Run the version 3 generator</a>

I still want to attempt to create a generator that draws mazes that are so random that I have never seen before and would have no clue how to solve the maze without tracing out the paths.