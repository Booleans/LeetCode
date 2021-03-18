'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    * MinStack() initializes the stack object.
    * void push(val) pushes the element val onto the stack.
    * void pop() removes the element on the top of the stack.
    * int top() gets the top element of the stack.
    * int getMin() retrieves the minimum element in the stack.

Methods pop, top and getMin operations will always be called on non-empty stacks.
'''

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # Append a tuple where tuple[0] is the value and tuple[1] is the current min value.
        # Allows accessing min value in constant time.
        if len(self.stack) > 0:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
