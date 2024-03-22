# time: O(nlgn)
# space: O(1)
from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        capacity = list(map(lambda i: capacity[i] - rocks[i], range(len(capacity))))
        capacity.sort()
        full_capacity = 0
        for num in capacity:
            if additionalRocks == 0 or num > additionalRocks: return full_capacity
            full_capacity += 1; additionalRocks -= num
        return full_capacity