class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # hold chars
        closingToOpen = {')': '(', '}' : '{', ']': '['} # hashmap to addociate closing parentheses with open ones

        for c in s:
            # If closing bracket
            if c in closingToOpen:
                # If stack is not empty and the top of the stack corresponds to the closing bracket
                if stack and stack[-1] == closingToOpen[c]:
                    stack.pop()
                else:
                    return False # Else, brackets are in incorrect order

            # Opening bracket
            else:
                stack.append(c)
        return True if not stack else False