class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        characters = set() # Hashset
        answer = 0
        for r in range(len(s)):
            # If we encounter duplicate, shrink window until there substring is valid again
            while s[r] in characters:
                characters.remove(s[left])
                left += 1
            characters.add(s[r])
            answer = max(answer, r - left + 1)
        return answer