# time: O(n^2)
# space: O(1) auxiliary space
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num_i in enumerate(nums):
            if num_i > 0:
                break
            if i and num_i == nums[i-1]:
                continue
            
            front, back = i+1, len(nums)-1
            while front < back:
                c_sum = num_i + nums[front] + nums[back]

                if c_sum < 0:
                    front += 1
                    continue

                if c_sum > 0:
                    back -= 1
                    continue

                while front < back and nums[front] == nums[front+1]:
                    front += 1
                while front < back and nums[back] == nums[back-1]:
                    back -= 1
                ans.append([num_i, nums[front], nums[back]])
                front += 1; back -= 1
        return ans