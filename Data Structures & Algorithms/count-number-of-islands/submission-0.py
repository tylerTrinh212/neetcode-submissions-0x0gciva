class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check for empty grid
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            # While queue not empty, expand island
            while q:
                row, column = q.popleft()
                # Directions to go up, left, down, right
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # If direction is within the grid and is a 1, use bfs on it
                for dr, dc in directions:
                    r, c = row + dr, column + dc
                    if (r in range(rows) and 
                    c in range(columns) and 
                    grid[r][c] == "1" and
                    (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
        
    
            



