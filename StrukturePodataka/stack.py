class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): # uzima prvi element steka bez da ga obrise
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

