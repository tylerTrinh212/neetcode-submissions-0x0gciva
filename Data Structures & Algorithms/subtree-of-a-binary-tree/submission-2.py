# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Subtree can end early
        if not subRoot:
            return True
        # Means we have exhausted entire tree
        if not root:
            return False
        # If tree contains subroot 
        if self.sameTree(root, subRoot):
            return True
        # Traverse root until we find a node with same value as subroot
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        

    def sameTree(self, root1, root2):
        # If both nodes null
        if not root1 and not root2:
            return True
        # If not null and equal values
        if root1 and root2 and root1.val == root2.val:
            return self.sameTree(root1.right, root2.right) and self.sameTree(root1.left, root2.left) 
        # If one is null or values not same
        else:
            return False
        