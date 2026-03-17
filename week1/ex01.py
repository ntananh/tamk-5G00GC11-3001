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
Function df
(max 1 XP)
---------------
Let us assume we have some states forming a state space in
which our AI agent operates. You do not know, e.g., how many
states there are. Each state has a unique string as its ID.
You also have an access to a successor function. When it gets
(as its parameter) the ID of a state, it returns a list containing
the IDs of the states in which the agent can continue from that
state ("successor states"). If the state has no such successor
states, an empty list is returned. (In tests, another successor
function will be used, but when implementing, you can use, e.g.,
the simple example implementation "example_successors(state_id)"
present in this file.)

Function df, when called and given the ID of the initial state
and the successor function as its parameters, should start from
the given initial state and return a list containing state IDs in
the order in which the corresponding states are visited when
performing a depth-first search applying preorder. You can
assume that you are effectively operating in a finite tree-like
state space, and thus, the execution should finally end, and
you do not need to deal with any loops or cycles. There are no
goal states. The mutual order of the successors of a state
returned by the successor function must be preserved when handling
them. (This order fixes the "left-to-right" order of the successor
states.)

N.B. The only way to get information about the state space is via
the successor function. You cannot, e.g., hardcode any information
about the states and their relations in your code (since it should
be possible to easily test your implementation with different,
desired state spaces).
"""

def example_successors(state_id):
    if state_id == 'C':
        return ['H', 'I', 'P']
    elif state_id == 'H':
        return ['M']
    elif state_id == 'I':
        return []
    elif state_id == 'P':
        return ['U', 'N']
    elif state_id == 'M':
        return []
    elif state_id == 'U':
        return ['K']
    elif state_id == 'N':
        return []
    elif state_id == 'K':
        return []
    else:
        return []


def df(state_id: str, successor_function: callable) -> list:
    result = [state_id]
    for child in successor_function(state_id):
        result += df(child, successor_function)
    return result

# You can test your implementation by calling, e.g.,
# df('C', example_successors). Remember to remove or comment out
# such calls before submitting your solution, though.





"""
Function climb
(max 1 XP)
---------------
(It is expected that you have implemented the df
function already or at least read the instructions.)
This time, you can assume there is available a helper function
that gives you a list of "neighboring" states of a given state.
This function works exactly like the previously described
successor function. However, now we do not assume having a
tree-like state space, but rather a more general state graph,
which may contain loops and cycles.

The function to be implemented, climb, gets this neighbors
function as its second parameter. Its third parameter is a
utility function that returns a numeric, nonnegative value
(utility) for each state, when called giving it the
corresponding state ID as its only argument. (State IDs are,
once again, strings.)

The function climb is to implement greedy local search
(hill-climbing) in its basic form – that is, from the candidate
states got from the neighbors function, one always selects
the one maximizing the value to become the next state of
interest (the one to proceed to), if the current utility
value can thus be improved.

The search starts from the state corresponding to the state ID
got as the first parameter. The function is to return a list
containing the encountered state IDs in the order they are handled;
the first item should be the ID of the start state, and whenever the
search moves to another state, the ID of this state should be appended
to the list. Finally, the last item of the list should be the ID of
the "best" state the search was able to find. If the starting state
is also the final state, the corresponding ID should be listed only
once.

Naturally, the values for the states are to be got from the utility
function and the neighbors from the neighbors function – do not
hardcode any such information about the states and their relations
in your code, but, instead, implement the functions you need for
testing, and use them when implementing the climb function.

Remember that when your implementation is going to be tested by
course staff, custom neighbors and utility functions will be used,
so make sure that your implementation works generally, when given
any neighbors and utility functions (that work as described)
as parameters.

"""

# You probably want to implement (for example, here) the utility
# function and the function returning the neighbors of a state
# for testing... They can be removed from the version to be
# submitted, though.


def climb(state_id: str, neighbors_function: callable, value_function: callable) -> list:
    return []  # replace this by your function body implementation!



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
"""



