class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])

        # Hash sets to show if visited ocean
        pacific, atlantic = set(), set()

        def dfs(r, c, visit, prevHeight):
            # Return if we've visited already, out of bounds, or the height is not acending.
            # We are going from the occean, so we are checking if it's greater than or equal to
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == rows or c == columns or
                heights[r][c] < prevHeight):
                return

            visit.add((r,c))
            # Run dfs in 4 directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(columns):
            dfs(0, c, pacific, heights[0][c]) # First row
            dfs(rows-1, c, atlantic, heights[rows-1][c]) # Last row

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0]) # First column
            dfs(r, columns - 1, atlantic, heights[r][columns-1]) # Last column

        # Combine both visit lists
        result = []
        for r in range(rows):
            for c in range(columns):
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])

        return result
