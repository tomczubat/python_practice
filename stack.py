
class Stack:
    def __init__(self):
        self.items = []
 
    def push(self, item):
        self.items.append(item)
 
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
 
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
 
    def is_empty(self):
        return len(self.items) == 0
 
    def size(self):
        return len(self.items)
    
    def print_items(self):
        print(self.items)
    

stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
stk.push(6)

print(stk.print_items)

