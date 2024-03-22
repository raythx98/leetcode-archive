# time: O(n)
# space: O(1)
from typing import List
class XORSolution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = 0
        for i in range(len(nums)+1):
            missing_num ^= i 
        for num in nums:
            missing_num ^= num 
        return missing_num
class APSolution:
    def missingNumber(self, nums: List[int]) -> int:
        # AP of [0, n] = n(n+1)/2
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)