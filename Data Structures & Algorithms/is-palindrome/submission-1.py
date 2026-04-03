class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Make new string with only characters and numbers
        new_string = ""
        for i in s:
            if i.isalnum():
                new_string += i.lower()

        # Set pointers at start and end of string
        left = 0
        right = len(new_string) - 1
        
        while left < right:
            # If they don't match, not a palindrome
            if new_string[left] != new_string[right]:
                print(new_string[left], new_string[right])
                return False
            left += 1
            right -= 1
        
        return True