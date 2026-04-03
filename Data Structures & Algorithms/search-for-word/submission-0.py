class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get size of board
        ROWS, COLUMNS = len(board), len(board[0])
        visit = set()

        def dfs(row, column, index):
            # Base case:
            if index == len(word):
                return True
            if (row < 0 or column < 0 
                or row >= ROWS or column >= COLUMNS 
                or board[row][column] != word[index] 
                or (row, column) in visit):
                return False
            
            visit.add((row, column))

            # Recursive calls in 4 directions
            result = (dfs(row - 1, column, index + 1) or
            dfs(row , column - 1, index + 1) or
            dfs(row + 1, column, index + 1) or
            dfs(row , column + 1, index + 1) )

            visit.remove((row,column))

            return result

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r, c, 0):
                    return True
        return False


