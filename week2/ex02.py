"""
GENERAL INSTRUCTIONS
--------------------


The idea shortly:
-----------------

Complete the bodies of the functions of this file 
so that they behave as described and submit this code 
file, retaining its original name and type, as your solution to 
the respective assignment submission area in Moodle.


Use of external libraries:
--------------------------

If you need/want, you are free to import libraries included 
in the standard Python distribution, but do not use any 
third party libraries (or such) that may not be present 
in the environment in which your work is going to be tested.


Reporting AI usage:
-------------------

At the end of this file, there is a dedicated place for you to 
report any use of AI tools in your work. If you have used any 
AI tools, please report the use there as instructed.

If you have not used any AI tools, please explicitly state that 
there as well. 

Always make sure that you have followed the instructions and 
course policy regarding the use of AI tools, that your work 
can be seen as your own work, and that you understand your 
code and can explain it if needed.

Neglecting to report the use of AI tools adequately may lead to 
XP penalties or fraud investigation, so please make sure to 
report the use of AI tools as required.


Further requirements, instructions, and info in more detail:
------------------------------------------------------------

- The test code used to check your solution will possibly move 
  or copy the submitted files and import and call your functions 
  expecting that the names and parameters are exactly as defined.
  Therefore:
  * Do not change the name of the file, compress it, or bury it 
    within any unrequested directories.
  * Do not change the names of the functions or their parameters.
    * Do not add extra parameters or alter the parameterization in 
      any way.
  * Make sure that the functions return the correct values having 
    correct types.
  * Do not call the functions automatically within this code file. 
    Naturally, you probably want to test your functions by calling 
    them yourself while developing your solution, but make sure to 
    remove such test calls (or comment them out) before submitting 
    your solution! (If both the test code and your own code call 
    the functions, this may lead to, e.g., unexpected prints and add 
    to the confusion making it more difficult to check your work.)

- Moreover, do not hardcode any solutions – the code should produce 
the correct results for all valid inputs.

- The submitted code must not produce any output (prints) when 
imported or when the functions are called, unless the function 
description specifically requires printing as part of the 
functionality. (Get rid of possible debugging prints that you may 
have used while developing your solution before submitting it.)

- If you need/want, you may create additional helper functions 
within this code file, if your solution uses them. However, 
only the functions defined below will be tested and graded.
If they call any helper functions you have defined, these helper 
functions must be defined within this same code file, and the rule 
of not producing any extra output applies to them as well. That is, 
they must not print anything either, except for the possible prints 
required by the instructions.

- Make sure that your code does not crash when the file is imported 
or when the functions are called with valid inputs! Otherwise, you
risk losing all the XPs for the exercise!
"""
###################################

"""
Function maze
(max 2 XP)
---------------
Function maze(file_path) reads a text file from the path given 
by the argument file_path. An example file (example_maze.txt) 
can be found in Moodle and may be used when implementing the 
function.

The file describes a rectangular maze/labyrinth such that the 
characters in the file correspond to elementary parts/locations 
– i.e., grid cells – of the maze. There are two types of these 
cells: passages and walls. Each normal passage cell is denoted by the 
character "." and each wall cell by "#".

The example below demonstrates possible content of a text file 
defining a maze. The file, in this case, has ten rows of of 47 
visible characters each. When your work is tested, the size and 
structure of the maze may vary. However, it is always enclosed by 
walls. (The lines here are presented in reading order – assume 
that the top line was read first from the file.)

###############################################
#...###.....######.............###......G...###
#.##....###.##.....###############.########.###
#S##.######.##.###...........#.......##.###.###
#....#......##.#############.#########........#
######.####.##.##.##.....###.###.....#.####.###
##.....#...###.......###.###.###.###.#.#.....##
##.#####.#.######.######.#######.#...###.###..#
##.......#...........#...........###.....####.#
###############################################

To point cell locations, we use the Cartesian (x, y) coordinate 
system with the following logic:
  x = character number: which character position on the line is 
      being examined?
  y = line number: which line are we on?
Counting starts from one.

One passage cell in the maze serves as the starting point. 
In the text file defining the maze, this cell is denoted by the 
character "S" instead of the "." character. (In the example maze 
above, this "S" is located at position (2, 4).)

In addition, the maze contains at least one goal cell. Goal cells 
are passage cells that are denoted in the text file by the character 
"G" instead of  the "." character. (You can assume that starting cell 
is not a goal cell.)

The aim is to find a shortest possible path from the start to a goal. 
The path length is the minimum number of steps required to traverse 
the path, and this length should be minimized by the choice of route. 
A step here means moving from a passage cell to an adjacent passage 
cell directly above, below, to the right, or to the left. (Steps 
cannot be taken diagonally, onto or into walls, or through walls.)

The function must return a list of pairs of numbers (tuples) listing 
the coordinates of the cells in the order in which they are reached 
when following the shortest path. (The list must not include the 
coordinates of the starting cell – start listing from the cell reached 
by the first step – but it must include the location of the goal cell 
reached (the last step on the path).

The returned list could thus look, e.g., like this: 
[(2, 3), (2, 2), (3, 2), (4, 2)]. 
(This particular sequence does not, in fact, lead to a goal in the 
case of the example maze – the cell (4, 2) is an ordinary passage 
cell – but this list is given just as an example to clarify the 
intended format of the returned list, not to provide a real solution 
even for that example maze.)

"""

from collections import deque

def maze(file_path: str) -> list:
    with open(file_path) as f:
        grid = [line.rstrip('\n') for line in f]
        start = (0, 0)
        for y, row in enumerate(grid):
            for x, ch in enumerate(row):
                if ch == 'S':
                    start = (x+1, y+1)

        queue = deque([start])
        came_from: dict[tuple[int, int], tuple[int, int] | None]  = {start: None}

    current = start
    while queue:
        current = queue.popleft()
        if grid[current[1] -1][current[0] -1] == 'G':
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            nx, ny = neighbor
            if neighbor not in came_from and grid[ny -1][nx -1] in '.G':
                came_from[neighbor] = current
                queue.append(neighbor)

    path = []
    while current != start:
        path.append(current)
        assert current is not None
        current = came_from[current]
    path.reverse()
    return path

          
# You can test your implementation by calling, e.g., 
# maze('example_maze.txt'). Remember to remove or comment out
# such calls before submitting your solution, though.




#########################
# AI tools usage report #
#########################
# Please report below any use of AI tools in your work.
# If you have used any AI tools, briefly describe what tools 
# have been used, how they have been used, and for what 
# purposes. If you have not used any AI tools, please 
# explicitly state that here as well. (Make sure that your 
# report is as comments or within a (multiline) string literal, 
# so that it does not produce any exceptions or other problems.)
"""
I used Claude to explain coordinate indexing for this task. I wrote the code myself step by step with hints
"""


