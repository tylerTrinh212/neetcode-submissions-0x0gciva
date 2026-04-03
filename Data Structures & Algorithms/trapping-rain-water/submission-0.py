class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Edge case
        if not height: return 0

        left = 0
        right = len(height) -1
        leftMax = height[left]
        rightMax = height[right]
        result = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                # Update leftmax
                leftMax = max(leftMax, height[left]) 
                result += leftMax - height[left]
            else:
                right -= 1
                # Update rightmax
                rightMax = max(rightMax, height[right])
                result += rightMax - height[right]
        return result