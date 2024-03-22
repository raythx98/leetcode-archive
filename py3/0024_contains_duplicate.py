# time: O(n)
# space: O(n)
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_freq = {}
        for num in nums:
            if num in nums_freq:
                return True
            else:
                nums_freq[num] = None
        return False