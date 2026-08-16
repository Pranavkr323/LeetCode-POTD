# LeetCode POTD - 2026-08-15
# 3702. Longest Subsequence With Non-Zero Bitwise XOR
# Approach: Bit Manipulation

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        zeros = True
        for num in nums:
            xor ^= num
            if num != 0:
                zeros = False

        if zeros:
            return 0

        return (n-1) if xor == 0 else n
