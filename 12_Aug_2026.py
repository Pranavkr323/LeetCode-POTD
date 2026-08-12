# LeetCode POTD - 2026-08-12
# 2958. Length of Longest Subarray With at Most K Frequency
# Approach: Sliding Window + HashMap

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        fq = {}
        max_len = 0

        for r in range(n):
            fq[nums[r]] = fq.get(nums[r], 0) + 1

            while fq[nums[r]] > k:
                fq[nums[l]] -= 1
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len
      
