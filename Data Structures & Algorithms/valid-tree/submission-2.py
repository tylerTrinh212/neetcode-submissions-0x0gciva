class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have n-1 edges
        if len(edges) > (n - 1):
            return False

        visit = set()
        adjList = {i: [] for i in range(n)}

        # Build adjacency list
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node, parent):

            if node in visit:
                return False

            visit.add(node)

            for child in adjList[node]:
                # Edges are undirected so ignore 
                if child == parent:
                    continue
                # If we revisit a node, there is a loop
                if not dfs(child, node):
                    return False

            return True

        return dfs(0, -1) and len(visit) == n # Check to make sure tree is not disconnected even if no cycle