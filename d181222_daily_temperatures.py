# time: O(n)
# space: O(n)
from typing import List
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_max = deque()

        for i in range(len(temperatures)-1, -1, -1):
            temp = temperatures[i]

            if not stack_max:
                temperatures[i] = 0
                stack_max.append((temp, 0))
                continue
            
            next_max, dist = stack_max[-1]
            next_dist = 1

            while next_max <= temp:
                stack_max.pop()
                next_dist += dist
                if not stack_max:
                    next_dist = 0
                    break
                next_max, dist = stack_max[-1]

            stack_max.append((temp, next_dist))
            temperatures[i] = next_dist

        return temperatures