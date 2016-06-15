import operator
 
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}
 
def evaluate_rpn(expression, stack):
    try:
 
        for token in expression.split():
            try:
                result = float(token)
            except ValueError:
                result = OPERATORS[token](stack.pop(-2), stack.pop())
            stack.append(result)
 
    except KeyError:
        print "Invalid input", repr(token)
    except IndexError:
        print "The stack is too small to apply the operator", repr(token)
 
if __name__ == "__main__":
    print "RPN.py - Press Control-D to exit."
 
    stack = []
 
    try:
        while True:
            evaluate_rpn(raw_input('%s> ' % stack), stack)
    except (KeyboardInterrupt, EOFError):
        print

