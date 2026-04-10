class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minimumStack = [] # Stack with minimum element on top for getMin

    def push(self, val: int) -> None:
        self.stack.append(val)

        self.minimumStack.append(min(min(self.stack), val))
        # self.minimumStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
