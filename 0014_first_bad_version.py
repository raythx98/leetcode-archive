# time: O(lgn)
# space: O(1)
def isBadVersion(version: int) -> bool:
    pass
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low