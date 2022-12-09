# time: O(lgn)
# space: O(n)
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + (high - low)//2 # left bias
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low if nums[low] == target else -1