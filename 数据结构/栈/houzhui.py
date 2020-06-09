"""
中缀表达式转后缀表达式.
用字典保存算术运算的优先级，将加减乘除的符号作为字典的键，优先级的数字作为字典的级别。
中缀表达式形如：(A+B)*C/D  遇到字母或者数字就直接输出。因为在后缀表达式中字母的顺序是不变的，所以可以直接把字母输出到我们想到的结果中。
遍历我们输入的表达式（字符串）
如果1.遇到字母，把字母直接拉到将要输出的列表中
如果2.遇到左括号，就把左括号压入栈中
如果3.遇到的是右括号，（说明字母我们肯定已经拉到列表中了），就把栈里面左括号之前的所有符号全都拉到列表中，列表中的符号优先级已经排好，不用管。
如果4.遇到算术运算符（除上述三种如果外就剩下这一个选择），如果栈是空的，就直接把算术运算符压进栈里面，如果遇到栈非空，就比较一下优先级，如果栈顶的
     优先级大于等于新遇到的运算符，那就把栈顶的运算符给弹出到列表里面，再把这个新遇到的运算符给压进栈里面。如果栈顶的优先级低，那就直接把新的运算符压进栈里面。
遍历完后，如果栈非空，就把所有的符号挨个弹出到列表中。
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
    tokenList = list(infixexpr)
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

print(infixToPostfix('(A+B)*C*(D/E)'))