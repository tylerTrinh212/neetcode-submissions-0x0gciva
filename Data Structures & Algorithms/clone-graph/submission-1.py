"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Use DFS to clone graph
        newList = {} # Map of nodes

        # Early return if no nodes
        if not node:
            return None

        def DFS(node):
            # Base case: If we've seen node already return its clone
            if node in newList:
                return newList[node]

            # Copy node value 
            newNode = Node(node.val)
            newList[node] = newNode

            # Copy neighbors
            for neighbor in node.neighbors:
                newNode.neighbors.append(DFS(neighbor))
            return newNode

        return DFS(node) 