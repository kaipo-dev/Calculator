# list of operators and their precedence
operators = {'+':0, '-':0, '*':1, '/':1, '^':2, '(':3, ')':3}

# following algorithm using associativity (left-to-right) framework instead of BIDMAS
# meaning if operators have equal precedence then it will prioritse left to right

''' PSUEDOCODE for Shunting Algorithm
1.  While there are tokens to be read:
2.        Read a token
3.        If it's a number add it to queue
4.        If it's an operator
5.               While there's an operator on the top of the stack with greater precedence:
6.                       Pop operators from the stack onto the output queue
7.               Push the current operator onto the stack
8.        If it's a left bracket push it onto the stack
9.        If it's a right bracket 
10.            While there's not a left bracket at the top of the stack:
11.                     Pop operators from the stack onto the output queue.
12.             Pop the left bracket from the stack and discard it
13. While there are operators on the stack, pop them to the queue
'''

# converts infix equation to postfix notation
# allows for easier evaluation of equation
def shunting_algorithm(equation):
    operator_stack = []
    output_queue = []

    while len(equation) > 0:
        token = equation.pop(0)

        if token.isnumeric():
            output_queue.append(token)
        elif token in operators:
            if token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop(-1))
                operator_stack.pop(-1)
            else:
                if len(operator_stack) > 0 and operator_stack[-1] not in '()':
                    while operators[operator_stack[-1]] > operators[token]:
                        output_queue.append(operator_stack.pop(-1))
                operator_stack.append(token)

    while len(operator_stack) > 0:
        token = operator_stack.pop(-1)
        output_queue.append(token)

    return output_queue

# evaluates the postfix equation using the stack method
def evaluate_shunted_equation(equation):
    eval_stack = []

    while len(equation) > 0:
        token = equation.pop(0)

        if token.isnumeric():
            eval_stack.append(token)
    
        elif token in operators:
            num_2 = eval_stack.pop()
            num_1 = eval_stack.pop()

            res = perform_operation(num_1, num_2, token)
            eval_stack.append(res)

    return eval_stack

# list of operations to perform depending on operator given
def perform_operation(num_1_str, num_2_str, operator):
    num_1 = int(num_1_str)
    num_2 = int(num_2_str)

    match operator:
        case '+':
            return num_1 + num_2
        case '-':
            return num_1 - num_2
        case '*':
            return num_1 * num_2
        case '/':
            return num_1 / num_2
        case '^':
            return num_1 ^ num_2