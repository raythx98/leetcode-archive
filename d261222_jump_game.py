# time: O(n)
# space: O(1)
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for idx, num in enumerate(nums):
            if idx > max_jump: return False
            max_jump = max(max_jump, idx + num)
        return True