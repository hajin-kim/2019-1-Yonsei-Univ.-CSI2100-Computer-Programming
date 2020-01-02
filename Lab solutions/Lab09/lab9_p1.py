"""
lab9_p1
"""

# Required to use the stack module as given
import stack

inp = input('Enter parentheses and/or braces: ')

s = stack.getStack()
proper = True

# Make times to run while loop
i = 0
i_limit = len(inp)

while proper and i < i_limit:
    item = inp[i]

    # Left things will be had push
    if item == '(' or item == '{' or item == '[':
        stack.push(s, item)
    # Right things will be had pop and be found that it is matched properly
    else:
        top_stack = stack.top(s)
        if item == ')' and top_stack == '(':
            stack.pop(s)
        elif item == '}' and top_stack == '{':
            stack.pop(s)
        elif item == ']' and top_stack == '[':
            stack.pop(s)
        else:
            proper = False
    #
    # for item in inp:
    #     if item == '(' or item == '{' or item == '[':
    #         stack.push(s, item)
    #     elif item == ')' or item == '}' or item == ']':
    #         if item == stack.top(s):
    #             stack.pop(s)
    #

    # While loop will be run len(inp) times
    i += 1

# Print the result that is proper or not
if s == [] and proper == True:
    print('Nested properly.')
else:
    print('Not properly nested.')
