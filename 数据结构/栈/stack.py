"""
括号匹配器：
表达式中需要判断括号是否正确使用，例如左括号与右括号的数量以及顺序是否正确。（（（）））类似这样判断这几个括弧是否被正确使用。
首先分析题目，可知，与第一个右括号相遇的左括号一定与第一个右括号是一对的，左括号与右括号是反序的关系。可以利用栈来实现这种反序的关系，
对一串括号进行逐个判断，如果是左括号就压入栈中，直到遇到右括号。（在栈中的始终是左括号）遇到右括号后，判断栈是否为空，如果栈为空，则说明不匹配，
如果不为空，说明栈中有左括号，则将一个左括号弹出。相当于一对一对地对括号进行判断。
"""


# 栈类：用列表来实现栈的功能。压入，弹出，查看栈顶的数据，查看栈是否为空，查看栈的大小。
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# 对输入的字符串进行判断以及压入弹出栈的操作
def parChecker(symbolString):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()
        index += 1
    if balance and s.isEmpty():
        return True
    else:
        return False


print(parChecker('(((()))()())'))
print(parChecker('(((()))()()'))