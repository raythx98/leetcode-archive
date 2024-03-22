# time: O(nlgk)
# space: O(k)
from heapq import heappop, heappush
from typing import List
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            return sqrt(x*x + y*y)
        heap_arr = []
        for point in points:
            heappush(heap_arr, (-distance(*point), point[0], point[1]))
            if len(heap_arr) > k:
                heappop(heap_arr)
        return [i[1:] for i in heap_arr]