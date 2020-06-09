"""
热土豆问题，有m个人，每次将土豆传递N次，传递完N次后手里有土豆的人出局，再接着传土豆，直到只剩下最后一人
"""


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotpotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotpotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))