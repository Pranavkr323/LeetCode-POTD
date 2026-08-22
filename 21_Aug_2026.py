# LeetCode POTD - 2026-08-21
# 3116. Kth Smallest Amount With Single Denomination Combination
# Binary Search, Inclusion - Exclusion

from itertools import combinations
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def valid_no(mid):
            count = 0

            for size in range(1, len(coins) + 1):
                for subset in combinations(coins, size):
                    lcm = 1

                    for num in subset:
                        lcm = lcm * num // gcd(lcm, num)
                        if lcm > mid:
                            break
                    if lcm > mid:
                        continue

                    ways = mid // lcm

                    if size % 2 == 1:
                        count += ways
                    else:
                        count -= ways

            return count
                

        low = min(coins)
        high = min(coins) * k

        while low <= high:
            mid = (low+high)//2
            if valid_no(mid) < k:
                low = mid + 1
            else:
                high = mid - 1

        return low


