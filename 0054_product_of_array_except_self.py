# time: O(n)
# space: O(1) auxiliary
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = nums.copy()
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            ans[i] = prod

        prod = 1
        for i in range(len(nums)-1):
            ans[i] = prod * ans[i+1]
            prod *= nums[i]
        ans[-1] = prod
        
        return ans