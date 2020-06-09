"""
已经将中缀表达式转化为后缀表达式，在此基础上，利用后缀表达式求值.
假如当前的操作环境只能实现加减乘除四种运算，如何利用简单的加减乘除来实现复杂长串还加括号的一条表达式，如A+(B*C)/D，可以先将其转化为
后缀表达式，再进行计算
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()     #相对于v1,这进行了修改，如果不加return，则只是对栈进行操作，list.pop()有返回值，为弹出的那个值。

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def infixToPostfix(infixexpr):
    prec = { '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    opStack = Stack()
    postfixList = []
    tokenList = list(infixexpr)          # 如果使用空格分开的字符串，可以用.split()方法来切割
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()]) >= prec[token]:
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


def postfixEval(postfxExpr):
    operandStack = Stack()
    tokenList = postfxExpr.split()

    for token in tokenList:
        if token in '0123456789':
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)

    return operandStack.pop()


def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    if op == '/':
        return op1 / op2
    if op == '+':
        return op1 + op2
    else:
        return op1 - op2

def get_result(expression):
    back_express = infixToPostfix(expression)
    result = postfixEval(back_express)
    return result

print(get_result('3+9*(7-5)*7'))

