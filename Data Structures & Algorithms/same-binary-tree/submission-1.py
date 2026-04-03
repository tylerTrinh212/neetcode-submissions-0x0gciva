# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null and the other is not
        if not q and not p:
            return True
        # If both not null and equal value
        if p and q and p.val == q.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(p.right, q.right)
        else:
            return False