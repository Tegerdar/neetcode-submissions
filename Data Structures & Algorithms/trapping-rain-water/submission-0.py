class Solution:
    def trap(self, height: List[int]) -> int:
        # without two pointers
        length = len(height)
        r_max, l_max = 0, 0
        total = 0
        l_maxes = [0] * length
        r_maxes = [0] * length
        for l in range(length):
            l_max = max(height[l], l_max)
            l_maxes[l] = l_max
        for r in range(length - 1, -1, -1):
            r_max = max(height[r], r_max)
            r_maxes[r] = r_max
        for i in range(length):
            total += min(l_maxes[i], r_maxes[i]) - height[i]
        return total