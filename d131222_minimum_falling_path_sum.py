# time: O(n^2)
# space: O(1)
from sys import maxsize
from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for cr in range(n-2, -1, -1):
            for cc in range(n):
                min_btm = maxsize
                for x, y in ((1, -1), (1, 0), (1, 1)):
                    nr, nc = cr+x, cc+y
                    if 0 <= nr <= n-1 and 0 <= nc <= n-1:
                        min_btm = min(min_btm, matrix[nr][nc])
                matrix[cr][cc] += min_btm
        return min(matrix[0])