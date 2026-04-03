class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip invalid char with left pointer
            while left < right and not self.isalphaNum(s[left]):
                left += 1

            # Skip invalid char with right pointer
            while left < right and not self.isalphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    # Helper function to check if character is valid, needed for skipping char we don't care about
    def isalphaNum(self, x):
        return ((ord('A') <= ord(x) <= ord('Z')) or
        (ord ('0') <= ord(x) <= ord('9')) or
        (ord('a') <= ord(x) <= ord('z')))
