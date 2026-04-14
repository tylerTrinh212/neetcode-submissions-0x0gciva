class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Visit set for tracking in dfs
        visit = set()
        adjList = {i: [] for i in range(n)}

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(node):

            if node in visit:
                return False
            
            visit.add(node)
            # Run dfs on all neighbors of curr node, adding them to visit
            for neighbor in adjList[node]:
                if neighbor not in visit:
                    dfs(neighbor)
            
            return True
        
        # Track how many times we run dfs
        count = 0
        for node in range(n):
            if node not in visit:
                dfs(node)
                count += 1
        return count


        