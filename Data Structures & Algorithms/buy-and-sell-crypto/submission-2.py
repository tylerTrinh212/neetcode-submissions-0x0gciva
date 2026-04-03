class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy
        right = 1 # sell
        maxProfit = 0

        while right < len(prices):
            # If profitable
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            else:
                # If not profitable, means sell point is where we should buy instead
                left = right
            right += 1

        return maxProfit