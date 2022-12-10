# time: O(n)
# space: O(n) linear with number of strings
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix_idx = 0
        for letters in zip(*strs):
            if len(set(letters)) > 1:
                break
            common_prefix_idx += 1
        return strs[0][:common_prefix_idx]