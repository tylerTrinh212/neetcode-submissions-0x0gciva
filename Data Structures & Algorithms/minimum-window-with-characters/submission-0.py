class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        # Initialize count T
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        res = [-1,-1]
        resLength = float("infinity")
        l = 0 # left pointer
        for r in range(len(s)):
            c = s[r] # Current char
            window[c] = 1 + window.get(c, 0) # count number of characters

            # Increment if we've found char we need
            if c in countT and window[c] == countT[c]:
                have += 1

            # Once we have substring with the necessary characters, minimize the window as much as possible
            while have == need:
                # update our result
                if (r - l +1) < resLength:
                    res = [l,r]
                    resLength = (r - l + 1)
                # pop from the left of the window
                window[s[l]] -= 1
                # If we removed enough to not be equal to countT/necessary num of char
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1 # shrink window
        l, r = res
        return s[l : r + 1] if resLength != float("infinity") else ""
        
         

