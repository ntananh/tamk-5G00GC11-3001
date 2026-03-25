import numpy
from sklearn.linear_model import LinearRegression

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

You can use what has already been imported above. Moreover,
if you need/want, you are free to import libraries included 
in the standard Python distribution, but do not use any 
third party libraries (or such) that may not be present 
in the environment in which your work is going to be tested.


Reporting AI usage:
-------------------

At the end of this file, there is a dedicated place for you to 
report any use of AI tools in your work. Follow the instructions
there. Remember that you are not allowed to give the task 
instructions to any external AI tools (even for summaries or so)!

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
Function estimate_values_based_on_data (max 2 XP)
------------------------------------------------

Function gets a name of a CSV file as its data_file parameter and
reads the file. (It can be assumed that the file is found in the 
search path with just the filename.) 

The file contains two columns (x and y), in which there are values 
that are to be interpreted as floating-point numbers. Comma is used 
as the column delimiter, and the file does not contain a header row; 
the first row is already a data row. Each row defines a data point 
in the usual two-dimensional Euclidean space. 

Using the standard least squares method, the function fits a line 
y = kx + b (where k and b are the slope and y-intercept, 
correspondingly) to the data points read from the file.

The function returns a list of float values. They are the y-values 
of the line at the x-values of interest, which are given as a list 
in the x_values parameter. The order of the resulting, returned 
y-values should correspond to the order of the given x-values.

Example:
    The data.csv file could contain the following two rows:
    2,2
    4,3.
    In this case,
    estimate_values_based_on_data('data.csv', [5, 0, -2]) would return
    [3.5, 1., 0.] – or at least something very close to this.

Be careful to return a list (not, e.g., a numpy array or such). 
(Remember: you can check the type with the type function.)
"""

def estimate_values_based_on_data(data_file: str, x_values: list) -> list:
    pass  # implementation here
    


#########################
# AI tools usage report #
#########################
# Please fill the report below (within the multiline string).
# Put 'X' characters in the bracket boxes ('[]') according 
# to how you have (or have not) used AI tools. 
# If you have used any such tool(s), replace the '___' strings 
# with appropriate (brief) informational texts.
"""
I have used these AI tools (list): ___

How? ___

For what purposes? ___

[] I have not used any AI tools in my work.

[] I have given the task instructions to an external AI tool
for some purposes. This is forbidden and considered as 
a fraud, of which I should be aware already. The case will
be handled according to the TAMK policy on academic integrity.

[] I hereby guarantee that I have not given the task instructions 
to any external AI tool.
"""