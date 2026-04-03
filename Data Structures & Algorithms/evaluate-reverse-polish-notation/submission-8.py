class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum + firstNum)

            elif i == '-':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum - firstNum)

                
            elif i == '*':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(secondNum * firstNum)

            elif i == '/':
                firstNum = stack.pop()
                secondNum = stack.pop()
                stack.append(int(float((secondNum / firstNum))))
            # Defualt case, append numbers
            else:
                stack.append(int(i))

        return int(stack.pop())

