"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # First sort intervals by starting time
        # Then iterate through and check if ending time overlaps with next start time

        intervals.sort(key = lambda i: i.start)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > (intervals[i].start):
                return False
        return True