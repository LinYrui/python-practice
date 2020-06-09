"""
v2:除了对圆括号外，加入对方括号以及花括号的判断。
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
        return self.items.pop()     #相对于v1,这进行了修改，如果不加return，则只是对栈进行操作，list.pop()有返回值，为弹出的那个值。

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
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and s.isEmpty():
        return True
    else:
        return False


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    if opens.index(open) == closes.index(close):
        return True


print(parChecker('[()({()})()()]'))
print(parChecker('[{((()))()()}'))