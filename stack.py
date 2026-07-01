class Stack:
    def __init__(self):
        self.stack = []

    # push
    def push(self, value):
        self.stack.append(value)

    # pop
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    # peek
    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]

    # check if empty
    def is_empty(self):
        return len(self.stack) == 0

    # display
    def display(self):
        print(self.stack)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()