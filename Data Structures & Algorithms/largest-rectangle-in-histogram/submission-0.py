class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # index, height

        for i, h in enumerate(heights):
            start = i
            # If stack is nonempty and top value is greater than curr height, 
            # means we cannot extend anymore and must pop and calc maxArea
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))
        
        # Iterate through stack at end
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

            
