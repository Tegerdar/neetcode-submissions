from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # eating speeds
        k = 1
        k_max = max(piles)
        # binary search trough every possible answer
        ans = None
        while k <= k_max:
            mid_k = k + (k_max - k) // 2
            if self.isSolution(mid_k, piles, h):
                ans = mid_k
                k_max = mid_k - 1
            else:
                k = mid_k + 1
        return ans

    def isSolution(self, k: int, piles: List[int], h: int) -> bool:
        # Linear check with proposed speed
        for p in piles:
            h -= math.ceil(p / k)
            if h < 0:
                return False
        return True 