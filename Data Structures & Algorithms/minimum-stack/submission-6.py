class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minimumStack = [] # Stack with minimum element on top for getMin

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.minimumStack:
            self.minimumStack.append(val)
        else:
            # At each push, the current minimum from stack or val
            minimumVal = min(val, self.minimumStack[-1])
            self.minimumStack.append(minimumVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
