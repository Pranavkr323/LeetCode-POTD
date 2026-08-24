# LeetCode POTD - 2026-08-23
# 1927. Sum Game
# Math, Game Theory, Greedy

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        q_left = 0
        q_right = 0
        sum_left = 0
        sum_right = 0

        for i in range(n):
            if i <= n//2 - 1:
                if num[i] == '?':
                    q_left += 1
                else:
                    sum_left += int(num[i])
            else:
                if num[i] == '?':
                    q_right += 1
                else:
                    sum_right += int(num[i])

        diff = sum_left - sum_right
        if q_left == q_right:
            if diff == 0:
                return False
            else:
                return True
        
        if (q_left - q_right) % 2 == 1:
                return True

        elif q_left > q_right:
            max_compensation = 9 * ((q_left - q_right)//2)
            if max_compensation != -diff:
                return True
            else:
                return False

        else:
            max_compensation = 9 * ((q_right - q_left)//2)
            if max_compensation != abs(diff):
                return True
            else:
                return False
