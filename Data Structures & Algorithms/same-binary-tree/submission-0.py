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
        # If one node is null
        elif not q or not p:
            return False
        # If q or p are not equal
        if q.val != p.val:
            return False
        
        # Recursive calls to either left and right side
        isSameQ = self.isSameTree(q.left, p.left)
        isSameP = self.isSameTree(q.right, p.right)
        

        return False if isSameP == False or isSameQ == False else True