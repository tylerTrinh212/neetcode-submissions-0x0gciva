# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        # Initialize deque
        q = deque()
        q.append(root)
        
        while q:
            # Get length of queue before we add new children
            qLen = len(q)
            level = [] # List of nodes per level

            for i in range(qLen):
                node = q.popleft()
                if node: # If node is not null, append it to level and add its children to the queue for the next level
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                # If the level is not null, append it to result
            if level:
                result.append(level)

        return result