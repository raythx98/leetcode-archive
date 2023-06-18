# time: O(n)
# space: O(1)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if 'a' <= word[0] <= 'z':
            return all('a' <= x <= 'z' for x in word)
        return all('a' <= x <= 'z' for x in word[1:]) or all('A' <= x <= 'Z' for x in word[1:])