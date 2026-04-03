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
        # result = []
        # lengthString = 0
        # currString = ""
        # for index, char in enumerate(s):
        #     # Get length of next string
        #     if char.isdigit():
        #         lengthString = int(char)
        #         continue
        #     # Make a new string to add to results
        #     if char == "#":
        #         currString = ""
        #         continue
        #     # Decode string
        #     currString += char
        #     lengthString -=1

        #     if lengthString == 0:
        #         result.append(currString)
        #         currString = ""
        # return result
        res,i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j+1+length
        return res






