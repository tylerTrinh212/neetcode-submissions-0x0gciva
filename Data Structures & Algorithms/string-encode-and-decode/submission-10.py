class Solution:

    def encode(self, strs: List[str]) -> str:
        codedString = ""
        for i in strs:
            # Get length of string i
            length = str(len(i))
            codedString += length
            # Add # as separator character
            codedString += "#"
            # Then add string itself
            codedString += i
        return codedString

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            # Use length from multiple characters to handle more than single digit
            length = int(s[i:j])
            # Get string starting at after # to the length found
            res.append(s[j+1: j+1+length])
            # Move i pointer to after string
            i = j+1+length
        return res






