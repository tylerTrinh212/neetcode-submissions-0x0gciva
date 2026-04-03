class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minimumStack = [] # Store minimum at each value in stack
    
    # Push minimum current element to stack and current minimum
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minimumStack) == 0:
            self.minimumStack.append(val)
        else:
            if val < self.minimumStack[-1]:
                self.minimumStack.append(val)
            else:
                self.minimumStack.append(self.minimumStack[-1])



    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
