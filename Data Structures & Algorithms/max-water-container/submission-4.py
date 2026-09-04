class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            h = min(heights[r], heights[l])
            area = h * (r - l)
            ans = max(area, ans)
            if h == heights[r]: # if the min heigh is right
                r -= 1
            else: # min heigh is left
                l += 1
        return ans