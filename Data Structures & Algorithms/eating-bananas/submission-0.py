class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        result = right

        while left <= right:
            # Find mid point of rate
            k = (left + right) // 2
            hours = 0
            # Calculate time to eat all piles using current rate
            for i in piles:
                hours += math.ceil(i/k) # Time = pile/rate and rounded up to nearest hour
            # If rate finishes within given time, check rates less than and update current result is needed
            if hours <= h:
                result = min(result, k)
                right = k-1
            else:
                left = k+1
        
        return result
