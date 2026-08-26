# LeetCode POTD - 2026-08-25
# 3718. Smallest Missing Multiple of K
# set, simulation

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        lookup = set(nums)

        prod = k

        while prod in lookup:
            prod += k

        return prod
