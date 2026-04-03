class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        
        for i in prices:
            maxProfit = max(maxProfit, i - minBuy) # Sell on i 
            minBuy = min(i, minBuy)
        return maxProfit
            