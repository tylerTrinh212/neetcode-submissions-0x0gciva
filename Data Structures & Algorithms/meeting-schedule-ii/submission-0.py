"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # Populate start and end
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        s = 0
        e = 0
        count = 0
        result = 0

        while s < len(intervals):
            if start[s] < end[e]: # If start time is less, a new meeting has started
                s += 1
                count += 1
                
            else: # Else if the end time is equal to start or less than the next start, a meeting has ended
                e += 1
                count -= 1

            result = max(result, count)

        return result
