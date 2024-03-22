# time: O(n)
# space: O(n)
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def recurse(price_idx, has_bought):
            if price_idx >= len(prices):
                return 0
            if (price_idx, has_bought) in dp:
                return dp[(price_idx, has_bought)]
            action = 0
            if has_bought: # sell
                action = prices[price_idx] + recurse(price_idx+2, not has_bought)
            else: # buy
                action = -prices[price_idx] + recurse(price_idx+1, not has_bought)
            noaction = recurse(price_idx+1, has_bought)
            dp[(price_idx, has_bought)] = max(action, noaction)
            return dp[(price_idx, has_bought)]

        return recurse(0, False)