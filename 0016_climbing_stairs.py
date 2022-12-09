# time: O(n)
# space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        num_ways = 1
        for i in range(1, n):
            prev, num_ways = num_ways, num_ways + prev
        return num_ways