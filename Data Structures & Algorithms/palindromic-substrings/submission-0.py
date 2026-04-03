class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        resultLength = 0

        # Consider every char as start of palindrome
        for i in range(len(s)):
            # Odd length
            left, right = i, i
            # While in bound and palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            # Even length
            left, right = i, i+1
            # While in bound and palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1 
                right += 1

        return result