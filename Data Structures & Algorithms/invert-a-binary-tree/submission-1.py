# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        self.invertHelper(root)
        return root
        
    
    # Recursive function
    def invertHelper(self, node):
        
        if node == None:
            return
        temp = node.left
        node.left = node.right
        node.right = temp

        self.invertHelper(node.left)
        self.invertHelper(node.right)


        