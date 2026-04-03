# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        # Use DFS to navigate tree and append it to a array
        def DFS(root):
            if not root:
                result.append("N")
                return 
            result.append(str(root.val))
            DFS(root.left)
            DFS(root.right)
        
        DFS(root)
        # Add delimiter in result
        return ",".join(result)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        vals = data.split(",") # Remove delimitter

        def DFS():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i])) # Make new node
            self.i += 1
            node.left = DFS()
            node.right = DFS()  
            
            return node   
                   
        head = DFS()    
        return head
            

