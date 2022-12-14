# time: O(v + e)
# space: O(v)
from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if 'b' needs to be finished before 'a'
        # an outgoing edge points from b to a
        #  b -> a
        out_edges = {b:[] for b in range(numCourses)}
        in_order = {b:0 for b in range(numCourses)}
        for a, b in prerequisites:
            out_edges[b].append(a)
            in_order[a] += 1

        valid_courses = 0
        frontier = deque([k for k, v in in_order.items() if not v])
        while frontier:
            nxt = frontier.popleft()
            valid_courses += 1
            for node in out_edges[nxt]:
                in_order[node] -= 1
                if not in_order[node]:
                    frontier.append(node)

        return valid_courses == numCourses

