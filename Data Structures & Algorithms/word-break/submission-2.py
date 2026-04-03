class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means: can the substring s[i:] be segmented using wordDict      
        dp = [False] * (len(s) + 1)

        # Base case: empty string (past the end) is always valid
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1): # Iterate backwards
            for w in wordDict:
                # Check if word w fits starting at index i
                if (i + len(w)) <= len(s) and s[i: i+ len(w)] == w :
                    dp[i] = dp[i + len(w)] 
                    # If the remaining suffix after w is segmentable,
                    # then s[i:] is also segmentable
                if dp[i]: # Break early if we already found right word
                    break
                    
        return dp[0]