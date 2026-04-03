class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # key is character, value is count of character
        closingToOpen = { ')': '(', ']': '[', '}': '{'} # hashmap to link closing to open bracket

        for i in s:
            # If closing bracket
            if i in closingToOpen:
                # If stack is not empty and the last entry in the stack corresponds to the closing bracket
                if stack and stack[-1] == closingToOpen[i]:
                    stack.pop()
                else:
                # If stack is empty and we get a closing bracket first, we know it's false
                    return False  
            # If opening bracket
            else:
                stack.append(i)

        # Return True if stack is empty
        return True if not stack else False

