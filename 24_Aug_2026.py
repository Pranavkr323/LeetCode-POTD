# LeetCode POTD - 2026-08-24
# 1872. Stone Game VIII
# DP, Prefix Sum

from functools import lru_cache
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0]*(n+1)
        for i in range(1,n+1):
            prefix[i] = prefix[i-1] + stones[i-1]

        dp = [0] * (n + 1)
        dp[n] = prefix[n]

        for i in range(n - 1, 1, -1):
            dp[i] = max(prefix[i] - dp[i + 1], dp[i + 1])

        return dp[2]

        # @lru_cache(None)
        # def dp(i):
            
        #     if i == n:
        #         return prefix[n]

        #     gain = max(prefix[i] - dp(i+1), dp(i+1))
        #     return gain
        
        # return dp(2)
