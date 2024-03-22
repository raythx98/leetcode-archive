# time: O(v + e)
# space: O(v + e)
from typing import List
from collections import deque, defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # check if (undirected) graph is bipartite
        adj_list = defaultdict(list) # storing neighbours as edges
        for ai, bi in dislikes:
            adj_list[ai].append(bi)
            adj_list[bi].append(ai)
        
        explored = set()

        for i in range (1, n+1):
            if n in explored:
                continue

            is_blues = {n: True}
            frontier = deque([n])

            while frontier:
                curr_person = frontier.pop()
                curr_is_blue = is_blues[curr_person]
                explored.add(curr_person)
                for nb_person in adj_list[curr_person]:
                    if nb_person in explored:
                        continue

                    frontier.append(nb_person)

                    if nb_person not in is_blues:
                        is_blues[nb_person] = not curr_is_blue
                        continue
                    
                    if is_blues[nb_person] == curr_is_blue:
                        return False

        return True