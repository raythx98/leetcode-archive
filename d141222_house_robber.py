# time: O(n)
# space: O(1)
from typing import List
class DPSolution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2, prev = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            choose = nums[i] + prev2
            nochoose = prev
            prev2, prev = prev, max(choose, nochoose)
        return prev
class MemoizeSolution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def recurse(idx, nums):
            if idx >= len(nums):
                return 0

            if idx == len(nums)-1:
                return nums[idx]

            if idx in dp:
                return dp[idx]

            curr = max(recurse(idx+1, nums), nums[idx] + recurse(idx+2, nums))
            dp[idx] = curr
            return curr
        return recurse(0, nums)