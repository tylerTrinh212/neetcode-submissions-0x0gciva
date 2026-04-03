class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} # Cache

        def dfs(i):
            if i in dp: # If i is in dp or we're at end of string
                return dp[i]
            if s[i] == "0":
                return 0

            result = dfs(i + 1)
            
            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] =="2" and s[i+1] in "0123456")):
            # If there's a second digit and the starting digit is either a one or two 
            # with the second digit being 0-6 if 1st digit is a 2
                result += dfs(i + 2)
            dp[i] = result
            return result

        return dfs(0)