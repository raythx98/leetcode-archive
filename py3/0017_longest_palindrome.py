# time: O(n)
# space: O(n)
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = len(list(filter(lambda x:x % 2 != 0, Counter(s).values())))
        return len(s) - odds + bool(odds)