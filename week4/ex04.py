import matplotlib.pyplot as plt
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

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
Function regr_nn (max 3 XP)
------------------------------------
The function uses CSV files ex04train.csv and ex04validation.csv as
its data sources. (These files can be downloaded from Moodle.)
The files are to be read by referring to them with their filenames 
only, without any additional path specifications. (The files are 
expected to be located in the directory from which the code is run.)

You are to implement a neural network–based regression model 
using PyTorch. (About installing PyTorch locally, 
see https://pytorch.org/get-started/locally/.)

During the session, we saw how a classification model can be
implemented, but the implementation of a regression model is quite 
similar. The main differences are the loss function to be applied 
and the handling of the last layer of the network / interpretation 
of the value obtained from it.

The model is to predict the value of a single (continuous-valued) 
numerical target variable based on the value of a single numerical 
(continuous-valued) feature variable given as input. The model is 
to be trained using the data from the ex04train.csv file and its 
performance is to be evaluated using the data from the 
ex04validation.csv file. The files contain columns x and y, where x 
is the feature variable and y is the target variable.

Basic functionality (2 XP):
---------------------------
Implement the functionality of the function as outlined by the 
following steps:
1. Read the data from the CSV files ex04train.csv and 
   ex04validation.csv.
2. Prepare the data in a suitable format for PyTorch.
3. Define a neural network model with an input layer of one input 
   and an output layer of one output (since we are dealing with 
   only one feature variable and are predicting only one value) 
   and one or more hidden layers. Use appropriate (nonlinear) 
   activation functions (e.g., ReLU() or Tanh()) in the hidden layers.
   Try out different architectures (number of layers and number 
   of neurons in each layer) and activation functions.
4. Train the model using a suitable optimization algorithm (e.g., 
   Adam works here, too), the nn.MSELoss() loss function, and a 
   suitable number of epochs.
5. Estimate the performance of the model on the validation data using 
   mean squared error (MSE) as the performance metric.

Let the function regr_nn return the MSE value obtained on the 
validation data. This value should consistently be clearly smaller 
than 0.001. Implement a sufficiently accurate model to achieve this, 
but also try to keep the model simple, with a small number of layers 
and neurons, featuring a short training time, and not having 
over-the-top computational resource requirements. (XP reductions
are possible, if testing your implementation is not conveniently
doable with modest resources. Training should not take many seconds
– and definitely not several minutes, even on a low-end computer.)


Visualization (1 XP):
---------------------
Let the same function also visualize with a single scatter plot the 
* data points (true values) of the training data, 
* data points (true values) of the validation data, and 
* the model's predictions on the validation data,
each with a different color. It should be easy to see from the plot
how well the model fits the data, and all the three types of points 
should be clearly distinguishable from each other. Validation data
points should be plotted on top of the training data points, and the 
model's predictions should be plotted on top of all the other points.

N.B. 
This time it really is OK and expected that the function produces this
plot as part of its functionality. Use plt.show() to show the plot. 
(Even if in your development environment the plot happens to be 
shown even without calling plt.show(), in the testing environment this
will not, most probably, be the case, so make sure to call it.)

"""

def regr_nn() -> float:
    pass  # Replace this with your implementation.


#########################
# AI tools usage report #
#########################
# Please fill the report within the multiline string below.
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