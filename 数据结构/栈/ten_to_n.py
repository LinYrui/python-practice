"""
用除余法求十进制转换为二进制。将一个十进制的整数不断除二，第一次除以2后剩下一个整数以及一个余数，那个余数即为所求二进制数的最低位。再将剩下的整数
继续除以2，得到的余数为二进制的第二位，以此类推。直到剩下的整数为1，去其模为1.但是我们按照从左到右的顺序的话，第一位为最高位，所以使用一个栈来实
现次序反转。   可将除以2换成其他数字N，即可得到N十进制转换为N进制。(如下面代码所示)
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

# 将十进制转化为N进制
def divideByN(n, decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % n
        remstack.push(rem)
        decNumber = decNumber // n

    binString = ''
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideByN(8, 16))
