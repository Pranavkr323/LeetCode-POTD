# LeetCode POTD - 2026-08-19
# 1386. Cinema Seat Allocation
# Approach: Hashtable

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        rows = {}

        for r, c in reservedSeats:
            if r not in rows:
                rows[r] = set()

            rows[r].add(c)
            
        ans = (n - len(rows)) * 2
        
        for reserved in rows.values():
        
            left = True
            mid = True
            right = True

            for seat in reserved:
                if 2 <= seat <= 5:
                    left = False

                if 4 <= seat <= 7:
                    mid = False

                if 6 <= seat <= 9:
                    right = False
                 
            if left and right:
                 ans += 2
            elif left or right or mid:
                 ans += 1
             
        return ans 
