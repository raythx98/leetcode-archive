# time: O(n)
# space: O(1) auxiliary space
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        front, back, s_nums = 0, len(nums) - 1, []
        while front <= back:
            if abs(nums[front]) < abs(nums[back]):
                s_nums.append(nums[back]**2)
                back -= 1
            else:
                s_nums.append(nums[front]**2)
                front += 1
        return s_nums[::-1]