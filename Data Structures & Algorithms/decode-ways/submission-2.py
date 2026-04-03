class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1} # Cache

        for i in range(len(s) -1, -1, -1): # Iterate backwards
            if s[i] == "0": # Base case
                dp[i] = 0
            else:
                dp[i] = dp[i+1] # Get val of char ahead

            if (i + 1 < len(s) and (s[i] == "1" or 
                s[i] =="2" and s[i+1] in "0123456")):
            # If there's a second digit and the starting digit is either a one or two 
            # with the second digit being 0-6 if 1st digit is a 2
                dp[i] += dp[i+2]
        return dp[0]