# time: O(n)
# space: O(1)
from typing import List
class MooresCandidateVotingSolution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for num in nums:
            if count == 0:
                candidate, count = num, 1
            elif candidate == num:
                count += 1
            else: 
                count -= 1
        return candidate
class BitManipulationSolution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        mask = 1
        for i in range(16):
            bit_count = 0
            for num in nums:
                if num & mask:
                    bit_count += 1
            if bit_count > len(nums)//2:
                majority |= mask
            mask <<= 1
        return majority