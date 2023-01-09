# time: O()?
# space: O()
from typing import List
from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        backtrack = [None for i in range(n)]
        frontier = deque([(0, None)]); ans = []
        while frontier:
            next_node, prev = frontier.pop()
            backtrack[next_node] = prev
            if next_node == n - 1:
                #answer found, backtrack
                curr_ans = []; curr = n - 1
                while curr is not None:
                    curr_ans.append(curr)
                    curr = backtrack[curr]
                ans.append(reversed(curr_ans))
            for nb_node in graph[next_node]:
                frontier.append((nb_node, next_node))
        return ans