# time: O(n)
# space: O(n)
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = 0, len(intervals) - 1
        while left < len(intervals) and intervals[left][1] < newInterval[0]:
            left += 1
        while right >= 0 and intervals[right][0] > newInterval[1]:
            right -= 1
        merged_start, merged_end = newInterval[0], newInterval[1]
        if right - left + 1:
            merged_start, merged_end = min(merged_start, intervals[left][0]), max(merged_end, intervals[right][1])
        return intervals[:left] + [[merged_start, merged_end]] + intervals[right+1:]