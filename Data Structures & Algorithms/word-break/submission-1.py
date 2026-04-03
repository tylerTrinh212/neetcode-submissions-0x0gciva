class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] means: can the substring s[i:] be segmented using wordDict      
        dp = [False] * (len(s) + 1)
        
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1): # Iterate backwards
            for w in wordDict:
                # If enough characters and the substring matches
                if (i + len(w)) <= len(s) and s[i: i+ len(w)] == w :
                    dp[i] = dp[i + len(w)] 
                    # Get the dp of current index plus the length of matched word
                    # AKA Checks if we matched a previous word also, not just the one we're currently on
                if dp[i]: # Break early if we already found right word
                    break
        return dp[0]