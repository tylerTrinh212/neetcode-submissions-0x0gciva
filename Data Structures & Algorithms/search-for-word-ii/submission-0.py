class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            # Make new node
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(r, c, node, word):
            # Base case
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            
            # Appending character
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.isEnd:
                result.add(word)

            # Recursive calls
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")

        return list(result)
            

