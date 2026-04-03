class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        answer = 0

        left = 0
        maxf = 0 # max frequency of char
        for r in range(len(s)):
            # Count each char
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # Determine maximum frequency of a char

            while (r - left + 1) - maxf > k: 
            # Determine if window is valid by checking window size - most common char 
            #is less than k, we will replace any char except the most common one
                count[s[left]] -= 1
                left += 1
            answer = max(answer, r - left + 1) # answer is the maximum window size, window size includes characters replaced
        return answer
                