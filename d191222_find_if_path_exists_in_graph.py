# time: O(v+e)
# space: O(v+e)
from collections import defaultdict, deque
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for ui, vi in edges:
            adj_list[ui].append(vi)
            adj_list[vi].append(ui)

        frontier = deque([source])
        explored = set()

        while frontier:
            curr_v = frontier.pop()
            if curr_v == destination:
                return True

            explored.add(curr_v)
            for nb in adj_list[curr_v]:
                if nb not in explored:
                    frontier.append(nb)
        return False