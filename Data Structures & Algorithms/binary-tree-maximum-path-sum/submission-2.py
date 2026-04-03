# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        # Return max path without splitting
        def DFS(root):
            if not root:
                return 0

            leftMax = DFS(root.left)
            rightMax = DFS(root.right)
            leftMax = max(leftMax, 0) # do not include negative vals by replacing it to 0
            rightMax = max(rightMax, 0)

            # computer max path WITH split (aka subtree not including root)
            result[0] = max(result[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax) # return max path with no split
        
        DFS(root)
        return result[0]