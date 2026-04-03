class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currArea = 0
        maxArea = 0
        left = 0
        right = len(heights) -1

        # Idea: Iterate using 2 pointers to find area between 2 points
        # Area formula = height * width, so in this case currArea = right-left * min(height[left], height[right])
        # If height[left] < height[right], move height[left]

        while left < right:
            # Calculate area
            currArea = (right - left) * min(heights[left], heights[right])
            if currArea > maxArea:
                maxArea = currArea
            # Move left pointer
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return maxArea