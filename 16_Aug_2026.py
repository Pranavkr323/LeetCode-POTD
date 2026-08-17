# LeetCode POTD - 2026-08-17
# 2029. Stone Game IX
# Approach: Game Theory / Greedy

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        rem0, rem1, rem2 = 0, 0, 0

        for val in stones:
            if val % 3 == 0:
                rem0 += 1
            elif val % 3 == 1:
                rem1 += 1
            else:
                rem2 += 1

        def check(rem0, rem1, rem2):

            if rem1 == 0:
                return False

            rem1 -= 1

            length = 1

            pairs = min(rem1, rem2)

            length += pairs * 2

            rem1 -= pairs
            rem2 -= pairs

            if rem1 > 0:
                length += 1
                rem1 -= 1

            length += rem0

            return length % 2 == 1 and rem1 + rem2 > 0

        return check(rem0, rem1, rem2) or check(rem0, rem2, rem1)
