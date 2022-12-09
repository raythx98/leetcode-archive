# time: O(n)
# space: O(n)
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color, frontier = image[sr][sc], []
        if initial_color != color:
            frontier.append((sr, sc))
        while frontier:
            cr, cc = frontier.pop()
            image[cr][cc] = color
            for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                nr, nc = cr + x, cc + y
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == initial_color:
                    frontier.append((nr, nc))
        return image        
