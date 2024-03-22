# time: O(n)
# space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        val = { 
            'I': 1, 'V': 5, 'X': 10, 
            'L': 50, 'C': 100, 'D': 500, 'M': 1000, 
        }
        s, numeral = list(s), 0
        for i, c in enumerate(s[:-1]):
            if val[c] < val[s[i + 1]]:
                numeral -= val[c]
            else:
                numeral += val[c]
        return numeral + val[s[-1]]
