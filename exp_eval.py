from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ^ >> << or numbers

    Returns the result of the expression evaluation.

    Raises an PostfixFormatException if the input is not well-formed"""

    valueStack = Stack(30)
    operators = [">>", "<<", "**", "*", "/", "+", "-"]
    for char in input_str.split(" "):
        try:
            char = int(char)
            valueStack.push(char)
            continue
        except ValueError:
            try:
                char = float(char)
                valueStack.push(char)
                continue
            except ValueError:
                pass
        if char in operators:
            if valueStack.size() >= 2:
                firstOp = valueStack.pop()
                secondOp = valueStack.pop()
                if char == "+":
                    valueStack.push(secondOp + firstOp)
                elif char == "-":
                    valueStack.push(secondOp - firstOp)
                elif char == "/":
                    #Handles exception in case of division by zero
                    if firstOp == 0:
                        raise ValueError("Invalid divisor 0")
                    else:
                        valueStack.push(secondOp / firstOp)
                elif char == "*":
                    valueStack.push(secondOp * firstOp)
                elif char == "**":
                     valueStack.push(secondOp ** firstOp)
                elif char == ">>":
                    if type(firstOp) == float or type(secondOp) == float:
                        raise PostfixFormatException("Illegal bit shift operand")
                    else:
                        valueStack.push(secondOp >> firstOp)
                elif char == "<<":
                    if type(firstOp) == float or type(secondOp) == float:
                        raise PostfixFormatException("Illegal bit shift operand")
                    else:
                        valueStack.push(secondOp << firstOp)
                        
            #Handles case where there are not enough operands to perform the given operation
            else:
                raise PostfixFormatException("Insufficient operands")

        #Handles case where there is a character present that is neither an operator nor operand
        else:
            raise PostfixFormatException("Invalid token")

    #Handles case where there are too many operands in the postfix expression
    if valueStack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return valueStack.pop()


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """

    opPrecedence = { "+": 0, "-": 0, "*": 1, "/": 1, "**": 2, ">>": 3, "<<": 3 }
    postFix = ""
    opStack = Stack(30)
    for char in input_str.split(" "):
        try:
            int(char)
            postFix += char + " "
        except ValueError:
            try:
                float(char)
                postFix += char + " "
            except ValueError:
                pass
        if char == "(":
            opStack.push(char)
        elif char == ")":
            while opStack.peek() != "(":
                postFix += opStack.pop() + " "
            if opStack.peek() == "(":
                opStack.pop()
        elif char in opPrecedence.keys():
            while opStack.size() > 0 and opStack.peek() != "(" and ((char != "**" and opPrecedence.get(opStack.peek()) >= opPrecedence.get(char)) or (char == "**" and opPrecedence.get(opStack.peek()) > opPrecedence.get(char))):
                    postFix += opStack.pop() + " "
            opStack.push(char)
    for i in range(opStack.size()):
        postFix += opStack.pop() + " "

    return postFix[:-1]



def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    postFix = ""
    operators = [">>", "<<", "**", "*", "/", "+", "-"]
    stack = Stack(30)
    charList = input_str.split(" ")
    charList.reverse()
    for char in charList:
        try:
            int(char)
            stack.push(char)
        except ValueError:
            try:
                float(char)
                stack.push(char)
            except ValueError:
                pass
        if char in operators:
            if stack.size() > 1:
                op1 = stack.pop()
                op2 = stack.pop()
                opString = op1 + " " + op2 + " " + char
                stack.push(opString)

    return stack.peek()
