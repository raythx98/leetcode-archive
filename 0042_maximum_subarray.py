# time: O(n)
# space: O(1)
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        n_sum = nums[0]
        for num in nums[1:]:
            n_sum = max(num, n_sum + num)
            largest = max(n_sum, largest)
        return largest