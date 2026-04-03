class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Using sliding window, extend window when we find a char in s1 and shrink when we do not
        # If our window become the size of s1, we have our answer and return true
        # We need to count the number of times each char shows up to make sure it matches the same counts in s1

        if len(s1) > len(s2):
            return False
        
        # Count each instance of each char in s1
        countS1 = {}
        for i in range(len(s1)):
            countS1[s1[i]] = 1 + countS1.get(s1[i],0)

        left = 0
        countS2 = {}
        
        for r in range(len(s2)):
            # Count characters in s2 that are also in s1
            if s2[r] in countS1:
                countS2[s2[r]] = 1 + countS2.get(s2[r],0)
            # Check to ensure our window size never exceeds the size of s1
            while (r - left + 1) > len(s1):
                countS2[s2[left]] = countS2.get(s2[left], 0) - 1
                if countS2.get(s2[left],0) <= 0:
                    del countS2[s2[left]]
                left += 1
            # If we have the same characters as s1 in our window, return true
            if countS1 == countS2:
                return True

        return False  