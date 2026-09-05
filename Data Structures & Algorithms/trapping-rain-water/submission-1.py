class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers
        total = 0
        length = len(height)
        left, right = 0, length - 1
        r_max, l_max = height[right], height[left]
        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                total += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                total += r_max - height[right]
        return total