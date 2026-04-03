class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # Cache from 0... amount
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c]) # Build dp from past dp entries
                    # Ex: coin = 4, amount = 7, dp[7] = 1 + dp[3] where we use 1 coin of 4

        return dp[amount] if dp[amount] != amount + 1 else -1