class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        answer = 0

        left = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left +=1

            answer = max(answer, r - left + 1)
        return answer
                