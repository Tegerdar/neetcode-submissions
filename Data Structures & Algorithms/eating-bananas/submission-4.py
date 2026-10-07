from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating speeds
        lo = 1
        hi = max(piles)
        # binary search trough every possible answer
        ans = hi
        while lo <= hi:
            m = lo + (hi - lo) // 2
            if self.isSolution(m, piles, h):
                ans = m
                hi = m - 1
            else:
                lo = m + 1
        return ans

    def isSolution(self, k: int, piles: List[int], h: int) -> bool:
        # Linear check with proposed speed
        for p in piles:
            h -= ceil(p / k)
            if h < 0:
                return False
        return True 