class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(len(intervals)):
            # Non overlapping conditions

            # If new interval end time is less than curr interval start time, append
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:] # Return rest of rsult and intervals
            elif newInterval[0] > intervals[i][1]: # If new interval start time is less than curr interval end time
                result.append(intervals[i])
            # Overlapping Condition
            else: 
                # Merge newInterval continusously
                newInterval = [min(intervals[i][0], newInterval[0]), max(newInterval[1], intervals[i][1])]
            
        result.append(newInterval) # Add new interval at the end
        return result
