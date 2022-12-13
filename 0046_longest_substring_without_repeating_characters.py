# time: O(n)
# space: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_pos = {}
        f_ptr, longest = 0, 0
        for idx, char in enumerate(s):
            if char in letter_pos and letter_pos[char] >= f_ptr:
                f_ptr = letter_pos[char] + 1
            else:
                longest = max(longest, idx-f_ptr+1)
            letter_pos[char] = idx
        return longest