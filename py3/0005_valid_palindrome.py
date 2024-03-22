# time: O(n)
# space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1
        while front < back:
            while front < back and not s[front].isalnum():
                front += 1
            while front < back and not s[back].isalnum():
                back -= 1 
            if s[front].casefold() != s[back].casefold():
                return False
            front += 1; back -= 1
        return True