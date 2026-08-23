# LeetCode POTD - 2026-08-22
# 3622. Check Divisibility by Digit Sum and Product
# Math, Simulation

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        summ = 0
        prod = 1

        while n > 0:
            digit = n % 10
            summ += digit
            prod *= digit
            n //= 10

        return temp % (summ + prod) == 0
