class Stack():
    def __init__(self):
        self.arr = []
    
    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if not self.is_empty():
            return self.arr.pop()
        else:
            raise IndexError("underflow condition")

    def peek(self):
        if not self.is_empty():
            return self.arr[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.arr)==0
    
    def size(self):
        return len(self.arr)
    

stack = Stack()
stack.push(10)
print(stack.arr)
stack.push(20)
print(stack.arr)
stack.push(30)
print(stack.arr)
stack.push(40)
print(stack.arr)
stack.push(50)
print(stack.arr)

stack.pop()
print(f"val after popping : {stack.arr}")
print(stack.is_empty())
print(stack.peek())