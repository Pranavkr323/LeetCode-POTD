# LeetCode POTD - 2026-08-19
# 3471. Find the Largest Almost Missing Integer
# Approach: Hashmap

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_no = -1

        if k == 1:
            fq = {}

            for num in nums:
                fq[num] = fq.get(num, 0) + 1

            max_no = -1

            for num, freq in fq.items():
                if freq == 1:
                    max_no = max(max_no, num)

            return max_no
            
        if k == n:
            return max(nums)

        if nums.count(nums[0]) == 1:
            max_no = max(max_no, nums[0])

        if nums.count(nums[-1]) == 1:
            max_no = max(max_no, nums[-1])

        return max_no
        
        
