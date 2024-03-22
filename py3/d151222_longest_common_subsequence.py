# time: O(mn)
# space: O(min(m,n))
class DPSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r_len, c_len = len(text1), len(text2)
        if r_len < c_len:
            return self.longestCommonSubsequence(text2, text1)

        dp = [[0 for c in range(c_len+1)] for r_len in range(2)]
        for r in range(r_len-1, -1, -1):
            for c in range(c_len-1, -1, -1):
                if text1[r] == text2[c]:
                    dp[r%2][c] = 1 + dp[1-r%2][c+1]
                else:
                    dp[r%2][c] = max(dp[1-r%2][c], dp[r%2][c+1])
        return max(dp[r_len%2][0], dp[1-r_len%2][0])
class MemoizeSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def recurse(idx1, idx2):
            if (idx1, idx2) in dp:
                return dp[(idx1, idx2)]
            
            if idx1 >= len(text1) or idx2 >= len(text2):
                dp[(idx1, idx2)] = 0
                return 0

            elif text1[idx1] == text2[idx2]:
                dp[(idx1, idx2)] = 1 + recurse(idx1+1, idx2+1)
                return dp[(idx1, idx2)]
                
            else:
                dp[(idx1, idx2)] = max(recurse(idx1+1, idx2),
                    recurse(idx1, idx2+1))
                return dp[(idx1, idx2)]
                
        return recurse(0, 0)