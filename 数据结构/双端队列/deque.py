"""
双端队列以及回文词的判定
"""


class Deque:
    def __init__(self):
        self.items = []

    def addfront(self, item):
        self.items.append(item)

    def removefront(self):
        return self.items.pop()

    def addrear(self, item):
        self.items.insert(0, item)

    def removerear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addrear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removefront()
        last = chardeque.removerear()
        if first != last:
            stillEqual = False

    return stillEqual




n = input("输入需要判断是否为回文词的数据：\n")
print(palchecker(n))