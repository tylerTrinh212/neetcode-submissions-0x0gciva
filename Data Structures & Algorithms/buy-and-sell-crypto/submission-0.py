class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        # Track the maximum profit so far and the cheapest to buy
        for i in prices:
            maxProfit = max(maxProfit, i - minBuy)
            minBuy = min(i, minBuy)
        return maxProfit