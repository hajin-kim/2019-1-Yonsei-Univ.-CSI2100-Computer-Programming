"""
lab9_p2
"""

import stack
import sys

def operation(operator, operand_last, operand_second_last):
    """
    Operating function
    :param operator: operator
    :param operand_last: first popped operand
    :param operand_second_last: second popped operand
    :return: the result of operation
    """
    # Return result
    if operator == '+':
        return operand_second_last + operand_last
    elif operator == '-':
        return operand_second_last - operand_last
    elif operator == '*':
        return operand_second_last * operand_last
    elif operator == '/':
        return operand_second_last / operand_last

def termination():
    """
    Terminating function when evaluation error occurred
    :return: none
    """
    print('Evaluation error')
    sys.exit()
    # Do exit

operator = ('+', '-', '*', '/')

inp = str(input('Enter an RPN expression: '))

# About if input means terminating this program
while inp and not (inp not in '0123456789+-*/=' and len(inp) == 1):

    # If not oper
    for i in inp:
        if i not in '0123456789+-*/= ':
            termination()

    right_most_position = True

    oper_stack = stack.getStack()

    slot = inp.split()

    for item in slot:

        if not right_most_position:
            # print('right-most position')
            termination()

        if item in operator:
            operand_last = stack.pop(oper_stack)
            operand_second_last = stack.pop(oper_stack)
            if operand_second_last == None:
                # print('stack underflow')
                termination()
            else:
                stack.push(oper_stack, operation(item, operand_last, operand_second_last))
        elif item == '=':
            right_most_position = False
        else:
            stack.push(oper_stack, int(item))

    # The result will be stored on the last of oper_stack
    result = stack.top(oper_stack)

    # If result is None, it means the input is only one =
    # If oper_stack have more than 1 arguments, it means operator is not sufficient
    if result == None:
        # print('one =')
        termination()
    if len(oper_stack) > 1:
        # print('two or more')
        termination()
    if stack.top(slot) != '=':
        # print('no =')
        termination()

    if type(result) == float:
        if float.is_integer(result):
            result = int(result)
        else:
            result = format(result, '.2f')

    print('Value of expression:', result)

    inp = str(input('Enter an RPN expression: '))
