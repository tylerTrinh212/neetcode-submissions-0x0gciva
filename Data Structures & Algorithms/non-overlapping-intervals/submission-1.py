class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0]) # Sort by start time
        prevEnd = intervals[0][1] # Get the ending 
        result = 0    
        
        for start, end in intervals[1:]:

            if start >= prevEnd: # No overlap
               prevEnd = end
            else:
                result += 1
                prevEnd = min(end, prevEnd) # Essentially skip it by setting the prevEnd to lowest val 
        return result