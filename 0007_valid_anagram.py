# time: O(n)
# space: O(n)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        for c in t:
            if c not in s_count:
                return False
            s_count[c] -= 1
        return not any(i != 0 for i in s_count.values())