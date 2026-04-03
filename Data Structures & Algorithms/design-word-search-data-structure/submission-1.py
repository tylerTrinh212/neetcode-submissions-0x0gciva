class Node:
    def __init__(self):
        self.children = [None] * 26 
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in range(len(word)):
            # Make new node
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                curr.children[index] = Node()
            # Move down a level
            curr = curr.children[index] 
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                index = ord(word[i]) - ord('a')
                # Recursive case
                if word[i] == '.':
                    for child in curr.children: # Check every child node 
                        if child: # Make sure we only run on not Null children
                            if dfs(i+1, child):
                                return True
                    return False
                else:
                    if not curr.children[index]:
                        return False
                # Move down a level
                    curr = curr.children[index] 
            return curr.isEnd

        return dfs(0, self.root)
    