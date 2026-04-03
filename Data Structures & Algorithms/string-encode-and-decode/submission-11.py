class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = ""

        for i in strs:
            # Get length of curr string
            length = str(len(i))
            # Append length to coded string
            newString += length
            # Add delimitter
            newString += "#"
            # Add actual string
            newString += i
        return newString



    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i # Pointer to go in the substring
            while s[j] != "#":
                j += 1 # Increment until we find delimitter to get length of string
            length = int(s[i:j])
            result.append(s[j + 1: j + 1 + length]) # Append string from after delimmitter to its length
            i = j + 1 + length # Move beyond current substring
        return result

