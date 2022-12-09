# time: O(n)
# space: O(n)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, carry = list(a), list(b), 0
        result = []
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            assert 0 <= carry <= 3
            result.append(str(carry & 1))
            carry //= 2
        return ''.join(result)[::-1]