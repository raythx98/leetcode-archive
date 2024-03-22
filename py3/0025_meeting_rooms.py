# time: O(nlgn)
# space: O(n)
from heapq import heappush, heappop
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        h = []
        last_complete_ts = 0
        for interval in intervals:
            heappush(h, (interval.start, interval.end))
        while h:
            s, e = heappop(h)
            if s < last_complete_ts:
                return False
            else: 
                last_complete_ts = e
        return True