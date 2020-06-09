class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self, item):
        self.item.insert(0, item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.items)
