# time: O(n)
# space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_frontwards, x_backwards = x, 0
        while x_frontwards:
            x_backwards = x_backwards * 10 + x_frontwards % 10
            x_frontwards //= 10
        return x == x_backwards