# time: O(n)
# space: O(1)
import sys
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, max_profit = sys.maxsize, -sys.maxsize - 1
        for price in prices:
            if price < low:
                low = price
            if price - low > max_profit:
                max_profit = price - low 
        return max_profit