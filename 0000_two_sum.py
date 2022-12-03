# time: O(n)
# space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [i, seen[num]]
            seen[target - num] = i
