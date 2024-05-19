class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def is_empty(self):
        return True if len(self.values) == 0 else False
    
    def size(self) -> int:
        return len(self.values)
    
    def peek(self):
        if self.is_empty():
            print('Empty stack!')
            return None
        return self.values[-1]
    
    def pop(self):
        if self.is_empty():
            print('Empty stack!')
        else: return self.values.pop()
    

stack = Stack()
stack.push(10)
stack.push(12)
stack.push(14)

print(stack.size())
# 3
print(stack.is_empty())
# False
print(stack.peek())
# 14
print(stack.peek())
# 14
print(stack.pop())
# 14
print(stack.size())
# 2
print(stack.pop())
# 12
print(stack.pop())
# 10
print(stack.pop())
# Empty stack!
# None
print(stack.peek())
# Empty stack!
# None
print(stack.size())
0
print(stack.is_empty())
# True