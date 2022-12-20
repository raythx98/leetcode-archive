# time: O(v+e)
# space: O(v)
from collections import deque
from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        frontier = deque([0])
        explored = set()
        while frontier:
            curr_room = frontier.pop()
            explored.add(curr_room)
            for nb_room in rooms[curr_room]:
                if nb_room not in explored:
                    frontier.append(nb_room)
        return len(explored) == len(rooms)
