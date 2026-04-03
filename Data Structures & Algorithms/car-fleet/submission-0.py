class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = [[p,s] for p,s in zip(position, speed)] # array of pairs
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            stack.append((target - p) / s)

            # If time of one before is faster
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)