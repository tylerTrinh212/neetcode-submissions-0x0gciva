class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort by start time
        intervals.sort(key = lambda i:i[0])

        result = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = result[-1][1]
            # Case where end time of curr interval start time is less than result's end time
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end) # Only need to change the end time of the latest in result to merge
            else:
                result.append([start, end])

        return result