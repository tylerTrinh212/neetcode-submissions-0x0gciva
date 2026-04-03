class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for i in numSet:
            #check if its the start of a sequence
            if (i-1) not in numSet:
                length = 1
                # Iterate through set and increase sequence size
                while (i+length) in numSet:
                    length +=1
                longestSequence = max(length, longestSequence)
        
        return longestSequence