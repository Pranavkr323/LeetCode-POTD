# LeetCode POTD - 2026-08-17
# 1563. Stone Game V
# Approach: Game Theory / Greedy

from functools import lru_cache
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            if left == right:
                return 0

            total = sum(stoneValue[left : right + 1])
          
            left_sum = ans = 0

            for i in range(left, right):
                left_sum += stoneValue[i]
                right_sum = total - left_sum

                if left_sum < right_sum:
                    ans = max(ans, dp(left, i) + left_sum)

                elif left_sum > right_sum:
                    ans = max(ans, dp(i + 1, right) + right_sum)
                    
                else:
                    ans = max(ans, max(dp(left, i), dp(i + 1, right)) + left_sum)
            return ans

        n = len(stoneValue)
        return dp(0, n - 1)
