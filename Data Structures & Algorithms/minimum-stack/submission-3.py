class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minimumStack = [] # Store minimum at each value in stack
    
    # Push minimum current element to stack and current minimum
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If stack is empty
        if len(self.minimumStack) == 0:
            self.minimumStack.append(val)
        # Get minimum of top of min stack and current val to push
        else:
            minimum = min(val, self.minimumStack[-1])
            self.minimumStack.append(minimum)


    def pop(self) -> None:
        self.stack.pop()
        self.minimumStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumStack[-1]
