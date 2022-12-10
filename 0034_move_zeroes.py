# time: O()
# space: O()
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_seek = 0
        for i, num in enumerate(nums):
            if num != 0 and nums[zero_seek] == 0:
                nums[zero_seek], nums[i] = num, 0
                zero_seek += 1
            elif nums[zero_seek] != 0:
                zero_seek += 1