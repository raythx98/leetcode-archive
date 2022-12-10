# time: O(1)
# space: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        r_bits = 0
        for i in range(32):
            r_bits = r_bits << 1 | n & 1
            n >>= 1
        return r_bits