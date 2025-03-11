class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
            if (not self.full()):
                self.items.append(item)
            else:
                return None

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return len(self.items) -1
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit


    def search(self, target):
        for i in reversed(range(len(self.items))):
            if not target in self.items:
                return -1
            if self.items[i] == target:
                return len(self.items) - i -1
        
