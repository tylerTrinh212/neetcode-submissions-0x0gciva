# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        
        while curr or stack:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            # Pop leftmost/lowest
            curr = stack.pop()
            n += 1
            # If kth element, return value
            if n == k:
                return curr.val
            # After we visit left, go to right child
            curr = curr.right
        return -1
        