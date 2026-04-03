class Node():
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            # Get index of letter
            index = ord(word[i]) - ord('a')
            # Add child node
            if curr.children[index] == None:
                curr.children[index] = Node()
            # Navigate down a level
            curr = curr.children[index]
        # Set last as end of word
        curr.isEnd = True
            

    def search(self, word: str) -> bool:
        curr = self.root

        for i in range(len(word)):
            # Get index of letter
            index = ord(word[i]) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        if curr.isEnd == True:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in range(len(prefix)):
            # Get index of letter
            index = ord(prefix[i]) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

        
