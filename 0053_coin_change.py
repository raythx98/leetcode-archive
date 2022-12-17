# time: O(n*amount)
# space: O(amount)
from typing import List
from sys import maxsize
class DPSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp  =[[0 if (c == 0) else maxsize for c in range(amount+1)] for r in range(2)]
        for row in range(1, len(coins)+1):
            for col in range(1, amount+1):
                curr_row, next_row = row%2, 1-row%2
                nochoose = dp[next_row][col]
                choose_stay = choose_next = maxsize
                amount, coin = col, coins[row-1]
                if amount - coin >= 0:
                    choose_stay = 1 + dp[curr_row][col-coin]
                    choose_next = 1 + dp[next_row][col-coin]
                dp[curr_row][col] = min(nochoose, choose_stay, choose_next)
        return -1 if dp[row%2][-1] >= maxsize else dp[row%2][-1]
class MemoizeSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_ls = {}
        def dp(coin_idx, amount):
            if amount == 0:
                return 0
            if amount < 0 or coin_idx >= len(coins):
                return -1

            if (coin_idx, amount) in dp_ls:
                return dp_ls[(coin_idx, amount)]
            
            choose_next = dp(coin_idx, amount-coins[coin_idx])
            nochoose = dp(coin_idx+1, amount)
            
            choose_stay = dp(coin_idx+1, amount-coins[coin_idx])

            choose_next += 1 if choose_next != -1 else 0
            choose_stay += 1 if choose_stay != -1 else 0

            answers = list(filter(lambda x: x != -1, [choose_next, nochoose, choose_stay]))
            if not answers:
                dp_ls[(coin_idx, amount)] = -1
                return -1
            else:
                dp_ls[(coin_idx, amount)] = min(answers)
                return min(answers)
        return dp(0, amount)











