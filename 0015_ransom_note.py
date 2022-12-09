# time: O(n)
# space: O(n)
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = Counter(magazine)
        for c in ransomNote:
            if c not in letter_count or letter_count[c] <= 0:
                return False
            letter_count[c] -= 1
        return not any(i < 0 for i in letter_count.values())
