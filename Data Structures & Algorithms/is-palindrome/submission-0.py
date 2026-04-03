class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in s:
            if i.isalnum():
                new_string += i.lower()

        print(new_string)
        left = 0
        right = len(new_string) - 1
        
        while left < right:
            if new_string[left] != new_string[right]:
                print(new_string[left], new_string[right])
                return False
            left += 1
            right -= 1
        
        return True