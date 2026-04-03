class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [] # [temperature, index]
        answer = [0] * len(temperatures)
        
        for index, temperature in enumerate(temperatures):
            # while stack is nonempty and temperature is greater than top of stack, pop and update answer
            while stack and temperature > stack[-1][0]:
                stackT, stackInd = stack.pop()
                answer[stackInd] = (index - stackInd)
            stack.append([temperature, index])
        return answer