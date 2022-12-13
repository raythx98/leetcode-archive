# time: O(mn)
# space: O(1)
from typing import List
from collections import deque
import sys
class DPSolution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for r in range(m):
            for c in range(n):
                if not mat[r][c]:
                    continue
                up = mat[r-1][c] if r > 0 else sys.maxsize
                left = mat[r][c-1] if c > 0 else sys.maxsize
                mat[r][c] = 1 + min(up, left)

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if not mat[r][c]:
                    continue
                down = mat[r+1][c] if r < m-1 else sys.maxsize
                right = mat[r][c+1] if c < n-1 else sys.maxsize
                mat[r][c] = min(mat[r][c], down+1, right+1)
        return mat
class BFSSolution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        explored = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
        frontier = deque([(i, j, 0) for j in range(len(mat[0])) for i in range(len(mat)) if not mat[i][j]])
        while frontier:
            cr, cc, distance = frontier.popleft()
            if explored[cr][cc]:
                continue
            explored[cr][cc] = 1
            mat[cr][cc] = distance
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = cr+x, cc+y
                if not 0 <= nr < len(mat) or not 0 <= nc < len(mat[0]):
                    continue
                frontier.append((nr, nc, distance+1))
        return mat