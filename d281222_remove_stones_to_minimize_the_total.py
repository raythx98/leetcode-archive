# time: O(nlgn)
# space: O(n)
from typing import List
from heapq import heappush, heappop
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for num in piles:
            heappush(heap, -num)
        
        for i in range(k):
            next_num = -heappop(heap)
            next_num -= next_num>>1
            heappush(heap, -next_num)

        return sum(map(abs, heap))