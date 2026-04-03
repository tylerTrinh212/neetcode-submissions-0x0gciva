class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0

        # Consider every char as start of palindrome
        for i in range(len(s)):
            # Odd length
            left, right = i, i
            # While in bound and palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength:
                    result = s[left: right + 1]
                    resultLength = right - left + 1
                left -= 1
                right += 1

            # Even length
            left, right = i, i+1
            # While in bound and palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength: # If longest palindrome
                    result = s[left: right + 1]
                    resultLength = right - left + 1
                left -= 1
                right += 1

        return result
